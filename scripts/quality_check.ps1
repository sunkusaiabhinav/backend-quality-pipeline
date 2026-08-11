$ErrorActionPreference = "Stop"

Write-Host "================================="
Write-Host "  Backend Quality Pipeline"
Write-Host "================================="

Write-Host "`n[1/9] Black"
black --check .

Write-Host "`n[2/9] isort"
isort --check-only .

Write-Host "`n[3/9] Flake8"
flake8 .

Write-Host "`n[4/9] Pylint"
pylint app

Write-Host "`n[5/9] Mypy"
mypy app

Write-Host "`n[6/9] Bandit"
bandit -r app

Write-Host "`n[7/9] pip-audit"
pip-audit

Write-Host "`n[8/9] Trivy"
trivy fs .

Write-Host "`n[9/9] Pytest"
python -m pytest --cov=app

Write-Host "`n================================="
Write-Host "  ALL QUALITY CHECKS PASSED"
Write-Host "================================="