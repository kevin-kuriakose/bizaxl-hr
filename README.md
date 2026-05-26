# BizAxl HR

HR & People management for BizAxl ERP.

## Requires
- bizaxl_erp

## DocTypes
- BA Employee, BA Department, BA Designation, BA Employee Group
- BA Leave Type, BA Leave Allocation, BA Leave Application
- BA Attendance, BA Holiday List, BA Expense Claim

## Installation
```bash
bench get-app https://github.com/kevin-kuriakose/bizaxl-hr.git
bench --site yoursite install-app bizaxl_hr
bench --site yoursite migrate
```
