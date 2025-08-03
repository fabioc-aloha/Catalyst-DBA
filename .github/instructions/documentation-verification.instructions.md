# Documentation Verification and Link Integrity Instructions

**Context**: University web resource verification and documentation integrity maintenance protocols
**Activation Pattern**: **/*documentation*, **/*verification*, **/*links*, **/*integrity*, **/*cleanup*
**Last Updated**: August 3, 2025
**Domain Foundation**: DK-DOCUMENTATION-VERIFICATION.md (comprehensive verification methodologies and quality standards)

## 🎯 **Core Instruction Framework**

### **CRITICAL PRINCIPLE**: Maintain User Experience Continuity
When encountering broken or inaccessible URLs in academic documentation, prioritize user access to resources over perfect link accuracy. Always provide alternative access paths with clear contact instructions.

### **Verification Priority Hierarchy**
1. **Critical Systems First**: Dissertation management, student portals, essential academic services
2. **Primary Resources**: Library access, course materials, academic calendars
3. **Support Services**: IT help, writing centers, administrative contacts
4. **Enhancement Resources**: Additional tools, optional services, supplementary materials

## 🔍 **Systematic URL Verification Protocol**

### **Phase 1: Pattern-Based Discovery**
```bash
# Use grep_search to identify all university URLs
grep_search --pattern="university_domain\\.edu" --isRegexp=true
grep_search --pattern="[a-zA-Z]+\\.university_domain\\.edu" --isRegexp=true
```

**Analysis Steps**:
1. **Subdomain Categorization**: Group URLs by subdomain pattern (library., portal., etc.)
2. **Access Pattern Identification**: Determine which subdomains consistently fail
3. **Critical System Mapping**: Identify URLs essential for user workflows
4. **Alternative Path Research**: Find working alternatives for broken URLs

### **Phase 2: URL Testing and Classification**

**Working URL Standards**:
- Response code 200 (successful access)
- Content loads properly without redirection loops
- Relevant content matches link description
- User can complete intended action

**Broken URL Handling**:
- Document specific failure mode (404, timeout, redirect loop)
- Research working alternative on main university domain
- Prepare contact instruction for department-specific access
- Test alternative path for user experience quality

### **Phase 3: Strategic URL Replacement**

**Replacement Pattern Template**:
```markdown
- [Service Name](https://main.university.edu/academics/) - Service description (contact [department] for access)
```

**Critical System Emphasis**:
```markdown
- [Critical System](https://working.url/) - **REQUIRED**: Essential workflow description
- [Critical System](https://working.url/) - **START HERE**: Priority action description
```

## 📄 **Documentation Integrity Protocols**

### **Duplicate Content Detection**

**Systematic Search Patterns**:
```bash
# Identify duplicate section headers
grep_search --pattern="^## [🏫🚀📖🎯🔬🏢📊]" --isRegexp=true

# Find specific content duplications
grep_search --pattern="duplicate_content_phrase" --isRegexp=false
```

**Analysis Framework**:
1. **Header Inventory**: List all major section headers with line numbers
2. **Content Comparison**: Identify sections with identical or near-identical content
3. **Legitimacy Assessment**: Determine which instance represents intended content
4. **Removal Planning**: Plan precise removal to preserve legitimate content

### **Surgical Content Removal**

**Preparation Steps**:
1. **Boundary Identification**: Determine exact start and end lines of duplicate content
2. **Context Preservation**: Ensure removal doesn't break document flow
3. **Reference Verification**: Check that internal links remain valid after removal
4. **Backup Planning**: Consider version control implications

**Removal Execution**:
```markdown
# Use replace_string_in_file with precise boundaries
replace_string_in_file(
    oldString: "exact_content_including_context_lines",
    newString: "replacement_preserving_flow",
    filePath: "target_file_path"
)
```

## 🏫 **University-Specific Integration Standards**

### **TUW (Touro University Worldwide) Protocols**

**Verified Working URLs**:
- Main university: `https://www.tuw.edu/`
- Student portal: `https://portal.tuw.edu/portal/students/`
- DMS system: `https://doctorate.tuw.edu/` (CRITICAL for dissertations)
- Course catalog: `https://www.tuw.edu/academics/course-catalog/`

**Standard Broken URL Redirection**:
- Library services: Redirect to `https://www.tuw.edu/academics/` with library contact note
- Canvas LMS: Redirect to academics page with IT contact note
- Student services: Redirect to academics page with specific department contact
- Research resources: Redirect to academics page with library/research office contact

**Critical System Integration**:
```markdown
- [Doctorate Management System (DMS)](https://doctorate.tuw.edu/) - **REQUIRED**: All dissertation projects must be initiated here
```

### **Contact Information Standards**

**Department Contact Templates**:
- Library access: "contact library for access"
- IT services: "contact IT for Canvas access"
- Student services: "contact student services for access"
- Academic affairs: "contact registrar" or "contact program advisor"
- Research support: "contact IRB office" or "contact research office"

## 🔄 **Quality Assurance Workflows**

### **Post-Verification Testing**

**Comprehensive Verification**:
```bash
# Check for remaining broken URLs
grep_search --pattern="broken_domain_pattern" --isRegexp=true

# Verify single occurrence of major sections
grep_search --pattern="^## 🏫" --isRegexp=true

# Confirm critical systems are properly emphasized
grep_search --pattern="\\*\\*REQUIRED\\*\\*|\\*\\*START HERE\\*\\*" --isRegexp=true
```

**User Experience Testing**:
1. **Workflow Completion**: Can users complete essential tasks using provided links?
2. **Contact Path Availability**: Are alternative contact methods clearly provided?
3. **Critical System Access**: Can users access essential systems (DMS, student portal)?
4. **Documentation Flow**: Does document structure support logical user progression?

### **Maintenance Scheduling**

**Regular Verification Intervals**:
- **Quarterly**: Comprehensive URL verification for all university resources
- **Semester**: Critical system verification (DMS, student portal, course catalog)
- **Annual**: Complete documentation integrity review and cleanup
- **As-Needed**: User-reported broken links and accessibility issues

**Documentation Evolution**:
- Track university infrastructure changes affecting student access
- Monitor user feedback for documentation improvement opportunities
- Integrate new university resources as they become available
- Maintain consistency across parallel documentation files

## 🎯 **Implementation Guidelines**

### **When to Apply These Instructions**

**Automatic Activation**:
- File patterns matching university documentation (README.md, MANUAL-DBA.md)
- Content containing university URLs or resource references
- User requests for link verification or documentation cleanup
- Discovery of broken links during regular documentation review

**Manual Activation**:
- Annual documentation maintenance cycles
- University infrastructure change notifications
- User reports of inaccessible resources
- Preparation for new student cohort onboarding

### **Success Metrics**

**Verification Quality**:
- All university URLs either work correctly or have documented alternatives
- Critical systems (DMS, student portal) maintain 100% accessibility
- Contact information provides clear alternative access paths
- No duplicate major sections in documentation files

**User Experience Quality**:
- Users can complete essential academic tasks using provided resources
- Broken links don't create dead-end user experiences
- Critical workflow systems are clearly identified and emphasized
- Documentation supports efficient student academic progression

---

*Systematic documentation verification and integrity maintenance protocols ensuring high-quality university resource integration and user experience continuity.*
