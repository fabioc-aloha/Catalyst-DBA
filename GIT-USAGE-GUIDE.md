# Git Usage Guide for DBA Research

## Quick Start Commands

### Daily Research Workflow
```bash
# Check current status
git status

# View research timeline
git timeline

# View completed milestones
git milestone
```

### Academic Commit Categories
```bash
# Research methodology and data collection
git research "Complete interview protocol validation"

# Literature review updates
git literature "Add systematic review methodology section"

# Academic writing and dissertation
git writing "Draft Chapter 3 methodology framework"

# Cognitive architecture improvements
git cognitive "Enhance qualitative analysis workflow"

# Data analysis and findings
git data "Implement mixed-methods integration analysis"
```

### Advanced Git Operations
```bash
# Create feature branch for new research phase
git checkout -b literature-review-phase2

# Merge completed research back to main
git checkout main
git merge literature-review-phase2

# Tag important milestones
git tag -a "IRB-Approval" -m "IRB approval received - research can proceed"
git tag -a "Proposal-Defense" -m "Research proposal successfully defended"
```

## Academic Collaboration

### Committee Review Workflow
```bash
# Create branch for committee review
git checkout -b committee-review-round1

# After incorporating feedback
git add .
git commit -m "📝 WRITING: Incorporate committee feedback on methodology chapter"

# Merge back to main after approval
git checkout main
git merge committee-review-round1
```

### Backup and Recovery
```bash
# Create backup branch before major changes
git checkout -b backup-$(date +%Y%m%d)

# Return to previous state if needed
git checkout main
git reset --hard HEAD~1
```

## Best Practices

1. **Commit frequently** - Daily progress should be committed
2. **Use descriptive messages** - Follow the academic categories
3. **Tag milestones** - Mark important research phases
4. **Branch for reviews** - Separate branches for committee feedback
5. **Backup regularly** - Push to remote repositories for safety
