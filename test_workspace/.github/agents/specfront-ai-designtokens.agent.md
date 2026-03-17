---
execution_order: 4
description: "STEP 4: Generate frontend UI framework themes, design patterns, and component specifications from HTML implementations and design analysis. Creates framework-specific design systems and component libraries in markdown format."
dependencies:
  required_before: ["specfront-ai-design", "specfront-ai-html"]
  feeds_into: ["specfront-ai-api-contracts"]
handoffs:
  - label: Define API Contracts
    agent: specfront-ai-api-contracts
    prompt: Create API specifications for data requirements identified in UI components and design patterns
    send: true
  - label: Skip to Task Breakdown
    agent: specfront-ai-tasks
    prompt: Generate development tasks if API contracts are not needed for this project
    send: false
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

**UI Framework Detection**: Extract framework preference from user input:

- "tailwind" / "tailwindcss" → Generate Tailwind-compatible theme documentation
- "material" / "angular material" → Generate Material Design theme documentation
- "primeng" / "prime ng" → Generate PrimeNG theme documentation
- "bootstrap" → Generate Bootstrap-compatible theme documentation
- "chakra" → Generate Chakra UI theme documentation
- Default: Material Design (if no framework specified)

**Framework Variables**:

- `$UI_FRAMEWORK`: Detected framework (tailwind|material|primeng|bootstrap|chakra)
- `$THEME_FORMAT`: Framework-specific theme documentation format
- `$COMPONENT_PATTERNS`: Framework-specific component pattern documentation

## Outline

This agent generates focused frontend UI framework theme documentation by analyzing design inputs to create systematic theme specifications and design patterns optimized for modern frontend development.

**Multi-Source Input Analysis**:

- **Design Analysis**: Structured specifications from `.specify/memory/design-analysis.md`
- **HTML Implementations**: Working prototypes from `.specify/html/[design-name]/`
- **Visual Mockups**: Image-based design specifications and layouts

**Output Location**: All generated theme documentation is created in `.specify/designpattern/` directory with 5 standard markdown files.

## Standard Documentation Structure

**Core Files (Always Generated)**:

```
.specify/designpattern/
├── design-tokens.md        # Colors, typography, spacing tokens
├── component-patterns.md   # UI component specifications
├── theme-config.md        # Framework-specific theme setup
├── responsive-patterns.md  # Layout and breakpoint patterns
└── implementation-guide.md # Setup and usage documentation
```

Given HTML implementations, styles, and UI patterns, do this:

1. **Multi-Source Design Analysis**:

   **Primary Source Priority** (use the most comprehensive source available):

   a. **Design Analysis Priority**: Load `.specify/memory/design-analysis.md` if available
   b. **HTML Implementation Analysis**: Extract from `.specify/html/[design-name]/`
   c. **Visual Design Analysis**: If mockups or design files provided

2. **Generate Standard Documentation Files**:

   **File 1: Design Tokens** (`design-tokens.md`):

   ```markdown
   # Design Tokens

   _Core design system tokens for ${UI_FRAMEWORK}_

   ## Color System

   **Brand Colors**:

   - Primary: [Extracted main brand color with hex/usage]
   - Secondary: [Supporting accent colors]
   - Neutral: [Grayscale palette for backgrounds/text]
   - Semantic: [Success, warning, error, info colors]

   ## Typography Scale

   **Font Families**:

   - Primary: [Main UI font with fallbacks]
   - Monospace: [Code/technical content font]

   **Type Scale**:

   - Heading levels (h1-h6) with sizes and weights
   - Body text variations (large, regular, small)
   - Font weight specifications (light, regular, medium, bold)

   ## Spacing System

   **Base Unit**: [Foundation spacing unit]
   **Scale**: [4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px pattern]
   **Usage**: Component padding, margins, gaps

   ## Borders & Shadows

   **Border Radius**: [Consistent corner radius values]
   **Shadows**: [Elevation system for components]
   ```

   **File 2: Component Patterns** (`component-patterns.md`):

   ```markdown
   # Component Patterns

   _UI component specifications and interaction patterns_

   ## Button Components

   **Variants**: Primary, Secondary, Ghost, Danger
   **States**: Default, Hover, Focus, Active, Disabled, Loading
   **Sizes**: Small (32px), Medium (40px), Large (48px)

   ## Form Components

   **Input Fields**:

   - Text inputs with validation states
   - Select dropdowns with custom styling
   - Checkboxes and radio buttons
   - Toggle switches

   **Validation States**: Default, Focus, Valid, Invalid, Disabled

   ## Navigation Components

   **Patterns**:

   - Sidebar navigation (collapsed/expanded)
   - Breadcrumb trails
   - Tab navigation
   - Pagination controls

   ## Data Display

   **Table**: Header styling, row states, responsive behavior
   **Cards**: Content structure, shadows, hover effects
   **Lists**: Item styling, separators, interactive states

   ## Feedback Components

   **Status Indicators**: Badges, alerts, toasts, progress bars
   **Loading States**: Skeletons, spinners, progress indicators
   ```

   **File 3: Theme Configuration** (`theme-config.md`):

   ```markdown
   # ${UI_FRAMEWORK} Theme Configuration

   _Framework-specific theme setup and customization_

   ## Theme Setup

   **Installation**:

   - Required dependencies for ${UI_FRAMEWORK}
   - Configuration file structure
   - Import/initialization steps

   ## Color Configuration

   **${UI_FRAMEWORK} Format**:
   [Generate framework-specific color variable format]

   - Primary color scale implementation
   - Semantic color mappings
   - Dark mode color overrides

   ## Typography Configuration

   **Font Integration**:

   - Font loading strategy
   - Framework-specific font definitions
   - Typography utility classes/components

   ## Component Theming

   **Global Overrides**:

   - Framework component customization patterns
   - CSS custom properties usage
   - Theme switching implementation

   ## Responsive Configuration

   **Breakpoints**: Mobile (320px), Tablet (768px), Desktop (1024px)
   **Container**: Max-widths and responsive behavior
   ```

   **File 4: Responsive Patterns** (`responsive-patterns.md`):

   ```markdown
   # Responsive Design Patterns

   _Mobile-first responsive design specifications_

   ## Breakpoint Strategy

   **Mobile First (320px+)**:

   - Single column layouts
   - Touch-friendly interaction areas
   - Simplified navigation patterns

   **Tablet (768px+)**:

   - Multi-column layouts
   - Expanded navigation options
   - Optimized form layouts

   **Desktop (1024px+)**:

   - Full sidebar navigation
   - Complex data table displays
   - Multi-panel layouts

   ## Layout Patterns

   **Grid System**:

   - Container max-widths
   - Column specifications
   - Gutter spacing

   **Component Adaptations**:

   - Navigation responsive behavior
   - Form field stacking patterns
   - Table to card transformations
   - Button group arrangements

   ## Accessibility

   **Focus Management**: Tab order and focus indicators
   **Contrast**: WCAG AA compliance (4.5:1 text, 3:1 UI)
   **Touch Targets**: Minimum 44px touch areas
   ```

   **File 5: Implementation Guide** (`implementation-guide.md`):

   ````markdown
   # Implementation Guide

   _UI design layout and theming implementation using documented design patterns_

   ## Design System Integration

   **1. Design Token Implementation**:

   Reference: `design-tokens.md` for complete token specifications

   - **Color System**: Apply documented brand colors across UI layouts
   - **Typography Scale**: Implement heading hierarchy and text sizing from tokens
   - **Spacing System**: Use consistent spacing units for layout padding/margins
   - **Theme Variables**: Configure ${UI_FRAMEWORK} with extracted design tokens

   **2. Layout Foundation Setup**:

   Reference: `responsive-patterns.md` for breakpoint specifications

   - **Grid System**: Implement responsive grid using documented breakpoints
   - **Container Layouts**: Apply max-width containers and spacing patterns
   - **Viewport Adaptations**: Configure mobile-first responsive behavior

   ## Component Layout Implementation

   **3. UI Component Integration**:

   Reference: `component-patterns.md` for component specifications

   - **Button Layouts**: Implement documented button variants and sizing
   - **Form Layouts**: Apply consistent form field spacing and validation states
   - **Navigation Layouts**: Implement sidebar, breadcrumb, and tab navigation patterns
   - **Data Display**: Configure table, card, and list layout patterns

   **4. Framework Theme Configuration**:

   Reference: `theme-config.md` for ${UI_FRAMEWORK} setup

   - **Theme Provider Setup**: Initialize ${UI_FRAMEWORK} with design tokens
   - **Component Theme Overrides**: Apply custom styling to framework components
   - **Responsive Theme**: Configure breakpoint-aware theme switching
   - **Dark Mode Support**: Implement theme variant switching if documented

   ## Layout Implementation Workflow

   **Phase 1: Foundation Setup**

   ```bash
   # Install framework dependencies
   npm install [framework-packages]

   # Configure theme files
   cp .specify/designpattern/theme-config.md → src/theme/
   ```
   ````

   **Phase 2: Design Token Integration**
   - Import color tokens as CSS custom properties or framework variables
   - Configure typography tokens in theme configuration
   - Set up spacing scale for consistent component layouts

   **Phase 3: Layout Pattern Implementation**
   - Apply responsive grid system from documented patterns
   - Implement navigation layouts (sidebar, header, breadcrumb)
   - Configure container and content area layouts

   **Phase 4: Component Layout Assembly**
   - Build page layouts using documented component patterns
   - Apply consistent spacing using design token system
   - Implement responsive behavior per component specifications

   ## Layout Quality Standards

   **Visual Layout Consistency**:
   - **Spacing**: Use only documented spacing tokens from design-tokens.md
   - **Alignment**: Follow grid patterns from responsive-patterns.md
   - **Typography**: Apply type scale consistently across layout hierarchy
   - **Color Usage**: Maintain documented color relationships in UI layouts

   **Responsive Layout Behavior**:
   - **Mobile Layout**: Single-column, touch-friendly component arrangements
   - **Tablet Layout**: Multi-column with sidebar navigation patterns
   - **Desktop Layout**: Full sidebar, multi-panel component layouts
   - **Component Adaptation**: Tables→cards, navigation→hamburger menu

   **Theme Integration Validation**:
   - **Design Token Usage**: All spacing/colors reference documented tokens
   - **Component Consistency**: UI components follow documented patterns
   - **Framework Integration**: Theme properly configured in ${UI_FRAMEWORK}
   - **Layout Accessibility**: Focus order and contrast meet WCAG standards

   ## Common Layout Implementation Patterns

   **Page Layout Structure**:

   ```
   [Header Navigation]
   [Sidebar] [Main Content Area] [Optional Right Panel]
   [Footer]
   ```

   **Component Layout Hierarchy**:
   - **Container**: Max-width wrapper with responsive padding
   - **Grid Areas**: Defined regions for navigation, content, sidebar
   - **Component Spacing**: Consistent margins between UI sections
   - **Content Flow**: Logical reading order with proper semantic structure

   **Theme Switching Implementation**:
   - **Color Scheme Toggle**: Light/dark mode theme variable switching
   - **Layout Adaptations**: Responsive component size/spacing adjustments
   - **State Persistence**: User theme preference storage and application

   ```

   ```

3. **Update Standards for New Prototypes**:

   When processing new prototypes, **extend existing files** rather than creating new ones:
   - **New components** → Add to `component-patterns.md`
   - **New design tokens** → Update `design-tokens.md`
   - **Framework changes** → Modify `theme-config.md`
   - **Layout patterns** → Enhance `responsive-patterns.md`
   - **Setup changes** → Update `implementation-guide.md`

## Quality Guidelines

### Focused Documentation Approach

1. **5 Standard Files Only**: Never exceed the core file structure
2. **No Framework Duplication**: Single theme-config.md adapts to detected framework
3. **Incremental Updates**: New prototypes extend existing files with new sections
4. **Implementation-Ready**: Specifications ready for immediate development
5. **Accessibility-First**: WCAG compliance integrated throughout

### Content Standards

**Each File Must Include:**

- Clear section headers with consistent formatting
- Practical specifications (sizes, colors, spacing values)
- Framework-specific implementation notes
- Accessibility requirements where applicable
- Usage examples and guidelines

**Avoid:**

- Repetitive framework comparisons
- Duplicate color/typography documentation
- Multiple files for similar concepts
- Abstract design theory without practical specifications
