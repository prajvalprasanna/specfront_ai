---
execution_order: 7
description: "STEP 7: Create detailed implementation guidance and execute the development plan. Provides comprehensive guidance for Angular 19 with TypeScript and Angular Material based on all previous workflow steps, HTML prototypes, and design documentation."
dependencies:
  required_before: ["specfront-ai-tasks"]
  feeds_into: []
handoffs: []
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **HTML Prototype and Design Documentation Analysis**:
   - **REQUIRED**: Load HTML prototype documentation from `.specify/html/[design-name]/`
   - **REQUIRED**: Analyze design specifications from `.specify/memory/design-analysis.md` if available
   - **REQUIRED**: Load theme documentation from `.specify/designpattern/` if available
   - **Extract implementation requirements**:
     - Component structure and hierarchy from HTML prototypes
     - Styling patterns and CSS implementations
     - Interactive behaviors and state management requirements
     - Responsive design patterns and breakpoints
     - UI framework integration points (Material, PrimeNG, Tailwind)
     - Design token usage and theme specifications
     - Accessibility patterns and ARIA implementations
   - **Validate consistency** between HTML prototypes, design documentation, and theme specifications
   - **Document UI requirements** for implementation phases

3. **Check checklists status** (if FEATURE_DIR/checklists/ exists):
   - Scan all checklist files in the checklists/ directory
   - For each checklist, count:
     - Total items: All lines matching `- [ ]` or `- [X]` or `- [x]`
     - Completed items: Lines matching `- [X]` or `- [x]`
     - Incomplete items: Lines matching `- [ ]`
   - Create a status table:

     ```text
     | Checklist | Total | Completed | Incomplete | Status |
     |-----------|-------|-----------|------------|--------|
     | ux.md     | 12    | 12        | 0          | ✓ PASS |
     | test.md   | 8     | 5         | 3          | ✗ FAIL |
     | security.md | 6   | 6         | 0          | ✓ PASS |
     ```

   - Calculate overall status:
     - **PASS**: All checklists have 0 incomplete items
     - **FAIL**: One or more checklists have incomplete items

   - **If any checklist is incomplete**:
     - Display the table with incomplete item counts
     - **STOP** and ask: "Some checklists are incomplete. Do you want to proceed with implementation anyway? (yes/no)"
     - Wait for user response before continuing
     - If user says "no" or "wait" or "stop", halt execution
     - If user says "yes" or "proceed" or "continue", proceed to step 4

   - **If all checklists are complete**:
     - Display the table showing all checklists passed
     - Automatically proceed to step 4

4. Load and analyze the implementation context:
   - **REQUIRED**: Read tasks.md for the complete task list and execution plan
   - **REQUIRED**: Read plan.md for tech stack, architecture, and file structure
   - **REQUIRED**: Cross-reference HTML prototype structure with task requirements
   - **REQUIRED**: Validate design pattern integration with planned architecture
   - **IF EXISTS**: Read data-model.md for entities and relationships
   - **IF EXISTS**: Read contracts/ for API specifications and test requirements
   - **IF EXISTS**: Read research.md for technical decisions and constraints
   - **IF EXISTS**: Read quickstart.md for integration scenarios
   - **Implementation Alignment Validation**:
     - Verify HTML prototype components match planned Angular components
     - Confirm CSS/styling approach aligns with chosen UI framework
     - Validate responsive design patterns from prototypes
     - Ensure accessibility requirements from design documentation are addressed
     - Check theme integration requirements from design pattern specifications

5. **Project Setup Verification with UI Framework Integration**:
   - **REQUIRED**: Create/verify ignore files based on actual project setup:

   **Detection & Creation Logic**:
   - Check if the following command succeeds to determine if the repository is a git repo (create/verify .gitignore if so):

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```

   - Check if Dockerfile\* exists or Docker in plan.md → create/verify .dockerignore
   - Check if .eslintrc\* exists → create/verify .eslintignore
   - Check if eslint.config.\* exists → ensure the config's `ignores` entries cover required patterns
   - Check if .prettierrc\* exists → create/verify .prettierignore
   - Check if .npmrc or package.json exists → create/verify .npmignore (if publishing)
   - Check if terraform files (\*.tf) exist → create/verify .terraformignore
   - Check if .helmignore needed (helm charts present) → create/verify .helmignore

   **If ignore file already exists**: Verify it contains essential patterns, append missing critical patterns only
   **If ignore file missing**: Create with full pattern set for detected technology

   **UI Framework Specific Patterns** (based on HTML prototype analysis and design documentation):
   - **Angular Material**: `.angular/`, `dist/`, `node_modules/`, `*.spec.ts.map`, `coverage/`
   - **Tailwind CSS**: `dist/`, `build/`, `tailwind.config.js.backup`, `*.css.map`
   - **PrimeNG**: `node_modules/primeng/`, `*.theme.css`, `custom-theme/`
   - **SCSS/SASS**: `*.scss.map`, `*.sass.map`, `.sass-cache/`

   **Common Patterns by Technology** (from plan.md tech stack):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `Makefile`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Tool-Specific Patterns**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

6. Parse tasks.md structure with HTML prototype requirements:
   - **Task phases**: Setup, Tests, Core, Integration, Polish
   - **Task dependencies**: Sequential vs parallel execution rules
   - **Task details**: ID, description, file paths, parallel markers [P]
   - **Execution flow**: Order and dependency requirements
   - **UI Implementation Requirements** (from HTML prototype analysis):
     - Component creation tasks based on HTML prototype structure
     - Styling implementation tasks following design patterns
     - Theme integration tasks using design token specifications
     - Responsive implementation tasks from prototype breakpoints
     - Accessibility implementation tasks from design documentation
     - Interactive behavior implementation from prototype interactions

7. Execute implementation following the task plan with HTML prototype adherence:
   - **Phase-by-phase execution**: Complete each phase before moving to the next
   - **HTML Prototype Validation**: Ensure each implemented component matches prototype structure
   - **Design Pattern Adherence**: Follow theme specifications and design documentation
   - **Respect dependencies**: Run sequential tasks in order, parallel tasks [P] can run together
   - **Follow TDD approach**: Execute test tasks before their corresponding implementation tasks
   - **File-based coordination**: Tasks affecting the same files must run sequentially
   - **UI Framework Integration**: Implement components using detected UI framework patterns
   - **Validation checkpoints**:
     - Verify each phase completion before proceeding
     - Validate HTML prototype structure is maintained in Angular components
     - Confirm styling matches design specifications
     - Ensure responsive behavior follows prototype patterns

8. Implementation execution rules with design adherence:
   - **Setup first**: Initialize project structure, dependencies, configuration, and UI framework integration
   - **Design System Integration**: Apply theme specifications and design tokens from design documentation
   - **Component Structure**: Create Angular components that match HTML prototype hierarchy
   - **Styling Implementation**: Apply CSS/SCSS following design patterns and UI framework guidelines
   - **Tests before code**: Implement tests that validate both functionality and design requirements
   - **Core development**: Implement models, services, CLI commands, endpoints with UI integration
   - **Interactive Behaviors**: Implement component interactions matching HTML prototype behaviors
   - **Responsive Implementation**: Apply responsive patterns from HTML prototypes
   - **Accessibility Features**: Implement ARIA patterns and accessibility features from design documentation
   - **Integration work**: Database connections, middleware, logging, external services
   - **Polish and validation**: Unit tests, performance optimization, documentation, design validation

9. HTML Prototype Compliance Validation:
   - **Component Structure Validation**:
     - Verify Angular component templates match HTML prototype structure
     - Confirm component hierarchy and nesting follows prototype patterns
     - Validate component props and data binding match prototype requirements
   - **Styling Validation**:
     - Ensure CSS classes and styling match design specifications
     - Verify responsive breakpoints and behavior match prototypes
     - Confirm theme integration follows design token specifications
   - **Interactive Behavior Validation**:
     - Test component interactions match prototype behaviors
     - Verify state management follows prototype interaction patterns
     - Confirm form validation and user feedback matches prototype
   - **Accessibility Validation**:
     - Verify ARIA attributes and semantic HTML follow prototype patterns
     - Test keyboard navigation matches prototype accessibility features
     - Confirm screen reader compatibility follows design documentation

10. Progress tracking and error handling with design validation:
    - Report progress after each completed task with design compliance status
    - Validate HTML prototype adherence at each implementation milestone
    - Halt execution if any non-parallel task fails or design requirements are not met
    - For parallel tasks [P], continue with successful tasks, report failed ones
    - Provide clear error messages with context for debugging and design discrepancies
    - Suggest next steps if implementation cannot proceed or design requirements conflict
    - **IMPORTANT** For completed tasks, make sure to mark the task off as [X] in the tasks file
    - **Design Compliance Tracking**: Document any deviations from HTML prototypes with justification

11. Completion validation with comprehensive design adherence:
    - Verify all required tasks are completed with HTML prototype compliance
    - Check that implemented components match HTML prototype structure and behavior
    - Validate styling implementation follows design specifications and theme documentation
    - Confirm responsive behavior matches HTML prototype responsive patterns
    - Validate accessibility implementation follows design documentation requirements
    - Ensure interactive behaviors match HTML prototype interactions
    - Verify UI framework integration follows design pattern specifications
    - Check that tests pass and coverage meets requirements including design validation
    - Confirm the implementation follows both technical plan and design documentation
    - Report final status with summary of completed work and design compliance verification

Note: This command assumes a complete task breakdown exists in tasks.md along with HTML prototypes in `.specify/html/` and design documentation in `.specify/designpattern/`. If any documentation is incomplete or missing, suggest running the appropriate specfront-ai agents first to regenerate the required documentation and prototypes.

## HTML Prototype Integration Guidelines

### Component Mapping Strategy

- **Direct Mapping**: Create Angular components that directly correspond to HTML prototype sections
- **Template Translation**: Convert HTML prototype templates to Angular component templates
- **Data Binding**: Implement Angular data binding for dynamic content shown in prototypes
- **Event Handling**: Translate prototype interactions to Angular event handlers

### Styling Implementation Strategy

- **CSS Extraction**: Extract and organize CSS from HTML prototypes into Angular component styles
- **Theme Integration**: Apply design tokens and theme specifications from design documentation
- **Framework Integration**: Convert prototype styling to chosen UI framework patterns (Material, PrimeNG, etc.)
- **Responsive Fidelity**: Maintain responsive behavior exactly as demonstrated in prototypes

### Behavioral Implementation Strategy

- **Interaction Patterns**: Implement all interactive behaviors shown in HTML prototypes
- **State Management**: Create Angular services and state management for prototype functionality
- **Form Handling**: Implement form validation and submission following prototype patterns
- **Navigation**: Create Angular routing that matches prototype navigation structure

### Quality Assurance for Design Adherence

- **Visual Regression Testing**: Compare implemented components with HTML prototype visuals
- **Responsive Testing**: Validate responsive behavior matches prototype across breakpoints
- **Interaction Testing**: Verify all prototype interactions work correctly in Angular implementation
- **Accessibility Testing**: Ensure accessibility features from prototypes are properly implemented
