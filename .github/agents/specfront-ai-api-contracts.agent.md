---
execution_order: 5
description: "STEP 5: Define API contracts for data requirements identified from UI components and design tokens. Creates comprehensive API specifications for backend integration."
dependencies:
  required_before: ["specfront-ai-design", "specfront-ai-html", "specfront-ai-designtokens"]
  feeds_into: ["specfront-ai-tasks"]
handoffs:
  - label: Break Down into Development Tasks
    agent: specfront-ai-tasks
    prompt: Generate sprint-ready development tasks based on design, clarifications, API contracts, and technical requirements
    send: true
  - label: Skip to Implementation
    agent: specfront-ai-implement
    prompt: Provide implementation guidance if no task breakdown is needed
    send: false
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## OpenAPI Processing Requirements

**CRITICAL**: Before generating any contracts, you MUST identify the OpenAPI JSON source. If not explicitly provided in the user input, ask the user to specify:

**OpenAPI Source Options:**

1. **File Path** - Path to existing OpenAPI JSON file in the workspace
2. **URL** - Remote OpenAPI specification URL
3. **Paste Content** - Direct OpenAPI JSON content
4. **Generate from Endpoints** - Create OpenAPI spec from existing endpoint definitions

**If OpenAPI source is not specified, respond with:**
"To generate accurate API contracts, please provide the OpenAPI specification:

1. **File Path**: Path to your OpenAPI JSON file
2. **URL**: Link to your OpenAPI specification
3. **Content**: Paste your OpenAPI JSON directly
4. **Endpoints**: List of endpoints to generate contracts for

Which option would you prefer?"

**Stop processing and wait for OpenAPI source before continuing.**

**OpenAPI Variables:**

- `$OPENAPI_SOURCE`: Source of OpenAPI specification (file|url|content|endpoints)
- `$API_VERSION`: API version from OpenAPI spec
- `$BASE_URL`: Base URL for API endpoints
- `$FEATURE_NAME`: Target feature name for contract generation

## Outline

This agent analyzes OpenAPI JSON specifications to generate comprehensive API contract documentation that serves as a detailed blueprint for backend integration. The agent creates thorough documentation capturing all API details including endpoints, versions, HTTP methods, properties, data types, validation rules, error handling, and enums using the standardized template format.

**Template Integration**: This agent uses the template file `.specify/templates/api-contracts-template.md` to ensure consistent documentation format and structure across all API contract specifications.

**Memory Integration**: This agent stores complete API contract documentation in `.specify/memory/api-contracts.md` with detailed endpoint specifications, data model definitions, and integration requirements for use during development.

Given an OpenAPI JSON specification, do this:

1. **Analyze OpenAPI Specification**:
   - Parse OpenAPI JSON structure and validate schema
   - Extract API metadata (version, title, description, base URL, servers)
   - Identify all endpoints with complete HTTP method details (GET, POST, PUT, DELETE, PATCH, OPTIONS)
   - Catalog all request/response schemas and data model structures
   - Document authentication requirements and security schemes with details
   - Extract custom headers, parameters, and middleware requirements
   - Identify deprecation status and versioning information

2. **Document Comprehensive Endpoint Details**:

   a. **Endpoint Specification Documentation**:
   - Document complete endpoint paths with path parameters
   - Specify HTTP methods with operation IDs and descriptions
   - Detail query parameters with types, required/optional status, and validation rules
   - Document request headers including authentication headers
   - Specify request body schemas with property details and data types
   - Document response schemas for all status codes (success and error)
   - Include response headers and content types

   b. **Request/Response Property Documentation**:
   - Document all request properties with exact data types and formats
   - Specify required vs optional properties with validation constraints
   - Detail nested object structures and array element types
   - Document property examples and default values from OpenAPI
   - Include format specifications (email, date-time, uuid, etc.)
   - Document string length limits, numeric ranges, and pattern constraints

   c. **HTTP Status Code and Error Documentation**:
   - Document all possible HTTP status codes for each endpoint
   - Specify error response structures and error message formats
   - Detail error code mappings and error type classifications
   - Document validation error responses with field-specific messages
   - Include authentication and authorization error responses
   - Specify rate limiting and timeout error handling

3. **Document Data Models and Schemas**:

   a. **Complete Data Model Documentation**:
   - Document all schema definitions from components/schemas section
   - Specify property names, data types, and format constraints
   - Detail object relationships and references between models
   - Document inheritance patterns and polymorphic model structures
   - Include computed properties and derived field specifications
   - Document data transformation and serialization requirements

   b. **Enumeration and Constant Documentation**:
   - Document all enum definitions with complete value lists
   - Specify enum value mappings and display names
   - Detail enum validation rules and acceptable values
   - Document constant values and configuration parameters
   - Include enum usage contexts and business rule constraints

4. **Generate API Contract Documentation**:

   Create comprehensive API contract documentation at `.specify/memory/api-contracts.md` following the template structure from `.specify/templates/api-contracts-template.md`:

   **Template Structure Requirements:**
   - Follow exact template format and section organization
   - Use consistent heading levels and documentation patterns
   - Include all required template sections with complete information
   - Maintain template styling and formatting conventions
   - Populate all template placeholders with actual API specification data

   **Documentation Content Requirements:**
   - **API Overview**: Complete API metadata, versioning, and base URL information
   - **Authentication**: Detailed security scheme documentation and token requirements
   - **Endpoint Catalog**: Comprehensive list of all endpoints with HTTP methods and descriptions
   - **Request Specifications**: Complete request documentation with parameters, headers, and body schemas
   - **Response Specifications**: Detailed response documentation with all status codes and schemas
   - **Data Models**: Full schema documentation with properties, types, and validation rules
   - **Error Handling**: Complete error response documentation with codes and message formats
   - **Validation Rules**: Comprehensive validation constraints and business rules
   - **Integration Requirements**: API usage patterns and integration guidelines

5. **Document Validation and Constraints**:
   - Extract and document all validation rules from OpenAPI schema constraints
   - Document required field validations and optional property handling
   - Specify format validations (email, phone, URL, date formats, etc.)
   - Document string length constraints, numeric ranges, and pattern matching
   - Detail custom validation rules and business logic constraints
   - Document array size limits and object nesting restrictions
   - Include cross-field validation rules and dependent property constraints

6. **Document API Versioning and Compatibility**:
   - Document API version information and versioning strategy
   - Specify backward compatibility requirements and breaking changes
   - Document deprecated endpoints and migration paths
   - Detail version-specific feature availability and constraints
   - Include API lifecycle information and sunset timelines

7. **Report Documentation Summary**:

   Provide a comprehensive summary including:
   - **OpenAPI Analysis**: Number of endpoints, models, schemas, and enums processed
   - **Documentation Coverage**: Complete coverage of all API specification elements
   - **Validation Rules**: Count of documented validation constraints and business rules
   - **Error Handling**: Comprehensive error response and status code documentation
   - **Data Models**: Complete schema documentation with relationship mapping
   - **Integration Readiness**: Assessment of documentation completeness for development

## Guidelines for API Contract Documentation Generation

### OpenAPI Processing Priority

**CRITICAL FIRST STEP**: Always identify and validate the OpenAPI JSON source:

1. **Check user input** for OpenAPI file paths or URLs
2. **If source provided**: Validate and process the OpenAPI specification
3. **If source NOT provided**: Stop and request OpenAPI source specification
4. **Parse and validate**: Ensure OpenAPI JSON is valid before processing

### Template Adherence Requirements

1. **Template Structure**: Strictly follow `.specify/templates/api-contracts-template.md` format
2. **Section Completion**: Fill all template sections with comprehensive API details
3. **Consistent Formatting**: Maintain template styling and markdown formatting
4. **Placeholder Replacement**: Replace all template variables with actual API data
5. **Documentation Depth**: Provide complete details for every documented element

### API Documentation Focus Areas

1. **Endpoint Documentation**: Complete HTTP method, path, and parameter documentation
2. **Data Type Specification**: Exact data type mapping with format specifications
3. **Validation Documentation**: Comprehensive constraint and business rule documentation
4. **Error Response Documentation**: Complete error handling and status code documentation
5. **Schema Relationships**: Clear documentation of data model relationships and dependencies
6. **Authentication Details**: Complete security scheme and authorization documentation

### When to Use This Agent

- You have an OpenAPI JSON specification requiring comprehensive documentation
- API contract documentation is needed for development team alignment
- Backend integration requirements need detailed specification
- API validation rules and constraints must be documented
- Error handling and response patterns need standardization
- Data model relationships require clear documentation

### Quality Focus for API Documentation

- **OpenAPI Compliance**: Documentation exactly reflects OpenAPI specification
- **Completeness**: Every endpoint, model, and constraint is documented
- **Accuracy**: All data types, formats, and validation rules are correct
- **Clarity**: Documentation is clear and unambiguous for developers
- **Consistency**: Template format is followed consistently throughout
- **Integration Ready**: Documentation provides complete implementation guidance

### OpenAPI Feature Coverage

- **HTTP Methods**: Complete documentation of GET, POST, PUT, DELETE, PATCH, OPTIONS
- **Authentication**: Bearer tokens, API keys, OAuth2 flows, and custom auth schemes
- **Request Formats**: JSON, form-data, query parameters, and multipart content
- **Response Handling**: Success responses, error responses, and all status codes
- **Data Types**: Strings, numbers, booleans, objects, arrays, enums, and custom formats
- **Validation**: Required fields, format validation, and custom business constraints
- **References**: Complete resolution of $ref components and shared schemas
- **Versioning**: API versioning strategies and compatibility documentation

### Integration with Other Agents

- **Primary Output**: Complete API contract documentation ready for development
- **Documentation Foundation**: Detailed specifications for service implementation
- **Validation Reference**: Comprehensive constraint documentation for form validation
- **Error Handling Guide**: Complete error response patterns for frontend handling
- **Data Contract**: Standardized data model documentation for type safety

**No code generation or implementation details are included - this agent focuses purely on comprehensive API contract documentation.**
