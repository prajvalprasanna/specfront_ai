---
execution_order: 2
description: "STEP 2: Clarify ambiguous requirements and design gaps identified during design analysis. Resolves unclear UI behaviors, data requirements, and interaction patterns before HTML generation."
dependencies:
  required_before: ["specfront-ai-design"]
  feeds_into: ["specfront-ai-html"]
handoffs:
  - label: Generate HTML Structure
    agent: specfront-ai-html
    prompt: Generate semantic HTML structure based on clarified design requirements and resolved ambiguities
    send: true
  - label: Skip HTML - Go to Design Tokens
    agent: specfront-ai-designtokens
    prompt: Extract design tokens if HTML generation is not needed
    send: false
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

This agent reviews the design analysis output from `/specfront-ai-design` and systematically resolves any ambiguous requirements, missing specifications, or unclear design elements before proceeding to HTML generation.

## Goal

Ensure all design requirements are clearly specified and unambiguous before moving to implementation phases. This prevents implementation delays and reduces the need for rework during later stages.

## Execution Steps

### 1. Load Design Analysis

- Read `.specify/memory/design-analysis.md` from the design agent output
- Extract any noted ambiguities, gaps, or clarification questions
- Review UI component specifications for missing details

### 2. Identify Clarification Areas

**Design System Gaps:**

- Missing color specifications or token definitions
- Unclear spacing and layout rules
- Incomplete typography specifications
- Missing responsive behavior definitions

**Component Behavior Gaps:**

- Unclear interaction states (hover, focus, active, disabled)
- Missing form validation rules and error states
- Unclear navigation patterns and user flows
- Missing accessibility requirements

**Data Requirements Gaps:**

- Unclear data binding requirements
- Missing API endpoint specifications
- Unclear data validation rules
- Missing loading and error states

### 3. Generate Clarification Questions

Create structured questions for each ambiguous area:

```markdown
## Design System Clarifications

### Colors & Theming

- [ ] What are the exact hex values for primary, secondary, and accent colors?
- [ ] Are there dark mode variants required?
- [ ] What are the semantic color mappings (success, warning, error)?

### Layout & Spacing

- [ ] What are the specific breakpoints for responsive design?
- [ ] What is the base spacing unit (4px, 8px, 16px)?
- [ ] How should components adapt between mobile and desktop?

## Component Behavior Clarifications

### Form Components

- [ ] What are the validation rules for each input field?
- [ ] How should error messages be displayed?
- [ ] What are the required vs optional field indicators?

### Navigation

- [ ] What is the exact navigation hierarchy?
- [ ] How should active/current page states be indicated?
- [ ] Are there breadcrumbs or progress indicators needed?

## Data & API Clarifications

### Data Sources

- [ ] What APIs or data sources will feed these components?
- [ ] What are the expected data formats and structures?
- [ ] How should loading states be handled?
```

### 4. Process User Responses

- Accept user input for clarification questions
- Update design specifications with resolved requirements
- Flag any remaining ambiguities that need further clarification

### 5. Generate Clarified Design Specification

Create an updated design specification that includes:

- Resolved design system tokens and specifications
- Clear component behavior definitions
- Specific data requirements and API specifications
- Updated UI patterns with resolved ambiguities

### 6. Validation

Ensure all major ambiguities have been addressed:

- Design system is completely specified
- Component behaviors are clearly defined
- Data requirements are unambiguous
- Responsive patterns are fully specified

## Output

The clarified design specification serves as the foundation for:

- HTML structure generation (`/specfront-ai-html`)
- Design token extraction (`/specfront-ai-designtokens`)
- API contract definition (`/specfront-ai-api-contracts`)

## Integration Notes

- This step can be skipped if the design analysis is already complete and unambiguous
- The agent should automatically identify when clarifications are not needed
- All clarifications should be documented for reference in later workflow steps
