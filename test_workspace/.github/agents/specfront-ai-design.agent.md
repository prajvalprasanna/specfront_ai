---
execution_order: 1
description: "STEP 1: Analyze UI mockups, wireframes, and Figma designs to extract detailed interface requirements, generate design templates, and create comprehensive design system analysis with framework-specific package requirements. This is the foundational step that feeds all subsequent workflow stages."
dependencies:
  required_before: []
  feeds_into: ["specfront-ai-clarify", "specfront-ai-html"]
handoffs:
  - label: Clarify Design Requirements
    agent: specfront-ai-clarify
    prompt: Review design analysis and resolve unclear UI behaviors, data requirements, and interaction patterns
    send: true
  - label: Generate HTML Structure (Skip Clarify)
    agent: specfront-ai-html
    prompt: Generate semantic HTML structure directly from design analysis if no clarifications needed
    send: false
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Framework Detection and Configuration

**CRITICAL**: The agent will automatically detect or determine the framework configuration from the current project context and user input. Framework detection follows these patterns:

**Auto-Detection from Project Context:**

1. **Check existing package.json and angular.json** for Angular projects
2. **Check package.json for React dependencies** (react, react-dom, next.js)
3. **Check package.json for Vue dependencies** (vue, @vue/cli, nuxt)
4. **Check existing configuration files** (tailwind.config.js, angular.json, vite.config.js)

**Framework Detection Priority:**

1. **Explicit user specification** in input (highest priority)
2. **Project configuration detection** from existing files
3. **Interactive framework selection** if none detected (fallback)

**Framework Variables (Auto-populated):**

- `$FRONTEND_FRAMEWORK`: Detected frontend framework (angular|react|vue|vanilla|other)
- `$UI_FRAMEWORK`: Detected UI framework (tailwind|bootstrap|material|antd|vanilla|other)
- `$VALIDATION_FRAMEWORK`: Recommended validation framework based on frontend choice
- `$I18N_FRAMEWORK`: Recommended internationalization framework
- `$TARGET_LOCALES`: Default to ['en-US'] unless specified
- `$CURRENT_PACKAGES`: Existing packages from package.json analysis

## Outline

This agent analyzes UI mockups, wireframes, Figma designs, and other visual design materials to extract comprehensive design requirements. It uses the existing design template from `.specify/templates/design-template.md` to generate a complete design analysis document that will be stored in `.specify/memory/design-analysis.md` for use by all other agents in the workflow.

**Template-Based Analysis**: The agent leverages the comprehensive design template structure to ensure consistent and thorough analysis covering all aspects from i18n requirements to Angular Material component specifications.

**Memory Integration**: All design analysis outputs are stored in `.specify/memory/design-analysis.md` as structured documentation that other agents can reference and build upon.

Given visual design materials or user descriptions, do this:

1. **Read and Load Design Template Structure**:

   Load the existing design template from `.specify/templates/design-template.md` to understand the required analysis structure and ensure consistency with established patterns.

2. **Detect Project Framework Configuration**:

   a. **Analyze Current Project**:

   ```bash
   # Check for existing configuration
   - Read package.json for existing dependencies
   - Check angular.json for Angular configuration
   - Look for configuration files (tailwind.config.js, etc.)
   - Detect current UI framework setup
   ```

   b. **Determine Framework Stack**:
   - **Frontend Framework**: Auto-detect from project files or user input
   - **UI Framework**: Check existing dependencies and configuration
   - **Validation Framework**: Recommend based on frontend framework
   - **i18n Framework**: Recommend based on frontend framework and requirements
   - **Target Locales**: Extract from user input or default to ['en-US']

3. **Generate Complete Design Analysis Document**:

   Using the `.specify/templates/design-template.md` structure, create a comprehensive analysis document at `.specify/memory/design-analysis.md`:

   ```markdown
   # Design Analysis: [FEATURE/PROJECT NAME]

   **Design Source**: [User input/mockup description]
   **Analyzed**: [Current Date]
   **Status**: Design Analysis Complete
   **Feature ID**: [Generated ID]

   ## Framework Configuration Detected

   - **Frontend Framework**: [Detected from project]
   - **UI Framework**: [Detected from project]
   - **Validation Framework**: [Recommended]
   - **i18n Framework**: [Recommended]
   - **Current Packages**: [List from package.json]
   - **Target Locales**: [From user input or default]

   ## Design Overview

   [Analysis based on user input following template structure]

   ## Internationalization (i18n) Requirements

   [Complete i18n analysis using template sections]

   ## Design System Architecture

   [Framework-specific architecture analysis]

   ## Visual Inventory

   [Component and page analysis following template]

   ## Implementation Recommendations

   [Framework-specific implementation guidance]

   ## Package Requirements

   [Specific packages needed based on detected framework]
   ```

4. **Framework-Specific Analysis Sections**:

   Based on the detected framework configuration, populate the relevant sections:

   a. **Angular Projects**:
   - Angular Material component analysis
   - Angular Router configuration requirements
   - Angular i18n setup and configuration
   - Angular CDK feature requirements

   b. **React Projects**:
   - Component library recommendations
   - React Router or Next.js routing setup
   - i18next configuration
   - State management recommendations

   c. **Vue Projects**:
   - Vue component library analysis
   - Vue Router configuration
   - Vue I18n setup
   - Vuex/Pinia state management

5. **Design Analysis Document Generation**:

   Create the complete design analysis document at `.specify/memory/design-analysis.md` with:
   - All sections from the design template filled out
   - Framework-specific implementation details
   - Package requirements and configuration
   - Component mapping and architecture
   - i18n requirements and setup
   - Implementation guidance for other agents

6. **Memory Document Structure**:

   The generated design analysis will serve as the source of truth for:
   - **HTML Generation Agent**: Component and layout specifications
   - **Styling Agent**: Design tokens and theme configuration
   - **Behavior Agent**: Interaction patterns and component behavior
   - **Content Agent**: i18n structure and content requirements
   - **Integration Agent**: Package requirements and framework setup

**Quality Assurance**:

- **Template Completeness**: All sections from design-template.md are addressed
- **Framework Accuracy**: Detected configuration matches project setup
- **Implementation Ready**: Provides actionable guidance for other agents
- **Memory Integration**: Document structure supports agent handoffs
- **Package Precision**: Specific versions and configurations provided
