# **Newman: Command-Line Postman Runner**

## **Overview**
Newman is a command-line tool that enables you to run Postman collections directly from your terminal or integrate them into automated systems, such as GitHub Actions, CI/CD pipelines, or other task runners, without requiring Postman's desktop application.

This guide provides a breakdown of how Newman processes your tests and a step-by-step setup guide to integrate Newman seamlessly into your automated testing workflow.

---

## **How Newman Processes API Tests**
Newman operates by performing the following steps:

1. **Reads the Postman Collection**  
   - Newman uses an exported JSON file of your Postman collection, which contains your API requests, URLs, headers, and predefined test scripts.

2. **Executes API Requests**  
   - It sequentially executes each API endpoint request defined in the Postman collection.

3. **Validates Assertions**
   - JavaScript test scripts written within your Postman requests are executed to verify if the API responses match your expectations. Examples of assertions include HTTP status validations (e.g., 200 OK) or response body checks.

4. **Outputs Test Reports**
   - Newman provides test results as:
     - **Console Output**: A pass/fail status reported directly to your terminal.
     - **Report Files** (if configured): JSON, HTML, or other formats for audit/compliance needs.

---

## **Step-by-Step Implementation Guide**

### **Step 1: Export Your Collection from Postman**
To integrate your existing API tests into Newman:
1. **Open Postman**: Launch your Postman desktop application.
2. **Locate Your Collection**: Right-click the API collection you wish to run via Newman.
3. **Export the Collection**: Choose the option to export the Collection in **v2.1 JSON format**.
4. **Store the Export File**: Move the exported JSON file into your GitHub repository. A suggested directory might be `tests/collections`.

---

### **Step 2: Install Newman**
Newman requires Node.js to run. Ensure it's installed in your environment. Then, install Newman globally:

```bash
npm install -g newman
```

Alternatively, to install Newman locally for use in your repository, include it as a development dependency:

```bash
npm install --save-dev newman
```

---

### **Step 3: Run Your Collection**
To test the exported collection:

1. **Basic Command**: Run Newman in your terminal:

   ```bash
   newman run <path-to-collection-json>
   ```

   Replace `<path-to-collection-json>` with the relative path to your JSON file, e.g., `tests/collections/my-api-collection.json`.

2. **Customize Execution**: Use flags for advanced options (e.g., environment files, detailed reports):

   ```bash
   newman run <path-to-collection-json> -e <environment-json> --reporters cli,html
   ```

   - `-e`: Passes an environment JSON file (if applicable).
   - `--reporters`: Specifies output formats, such as HTML reports.

---

### **Step 4: Integrate Newman into CI/CD**
Add Newman commands to your **GitHub Actions Workflow** or any other CI/CD pipeline you're using.

#### **Example GitHub Actions Workflow YAML**
Here's an example of a GitHub Actions configuration to automate Newman test runs:

```yaml
name: Newman Tests

on:
  push:
    branches:
      - main

jobs:
  newman-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install Newman
        run: npm install -g newman

      - name: Run Newman Tests
        run: |
          newman run tests/collections/my-api-collection.json --reporters cli,html \
          --reporter-html-export reports/newman-test-report.html
          
      - name: Upload HTML Report
        uses: actions/upload-artifact@v3
        with:
          name: Newman Test Report
          path: reports/newman-test-report.html
```

---

### **Step 5: Debug and Optimize**
- **Review Test Results**: Check console or report logs to debug test failures.
- **Refine Test Scripts**: Adjust JavaScript assertions to ensure coverage for edge cases.
- **Repeat**: Update your Postman collection and rerun Newman tests iteratively as your API evolves.

---

## **Resources**
- [Newman Documentation](https://www.npmjs.com/package/newman)
- [Postman Collections](https://learning.postman.com/docs/getting-started/creating-the-first-collection/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

This guide provides a concise, professional framework for adopting Newman within your automated API testing workflows.