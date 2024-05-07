<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">MEDICAL_COPILOT</h1>
</p>
<p align="center">
    <em>HTTP error 429 for prompt `slogan`</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/jrp2212/medical_copilot?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/jrp2212/medical_copilot?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/jrp2212/medical_copilot?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/jrp2212/medical_copilot?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/PostCSS-DD3A0A.svg?style=flat&logo=PostCSS&logoColor=white" alt="PostCSS">
	<img src="https://img.shields.io/badge/Autoprefixer-DD3735.svg?style=flat&logo=Autoprefixer&logoColor=white" alt="Autoprefixer">
	<img src="https://img.shields.io/badge/Sass-CC6699.svg?style=flat&logo=Sass&logoColor=white" alt="Sass">
	<img src="https://img.shields.io/badge/React-61DAFB.svg?style=flat&logo=React&logoColor=black" alt="React">
	<img src="https://img.shields.io/badge/Axios-5A29E4.svg?style=flat&logo=Axios&logoColor=white" alt="Axios">
	<br>
	<img src="https://img.shields.io/badge/ESLint-4B32C3.svg?style=flat&logo=ESLint&logoColor=white" alt="ESLint">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=flat&logo=TypeScript&logoColor=white" alt="TypeScript">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation & Setup](#-installation)
> - [ Contributing](#-contributing)


---

##  Overview

Medical Copilot aims to enhance the healthcare experience by automating the reading, analysis, and response to patient medical records and clinical guideline documents (i.e. patient intake forms), thereby alleviating the paperwork burden for nurses and doctors. This comprehensive pipeline enables healthcare professionals to devote more time and expertise to patient care. At its core, Medical Copilot seamlessly integrates patient medical record data and clinical guidelines through an intuitive interface. Leveraging cloud computing and LLMs, it distills complex information into concise summaries and diagnostic insights, facilitating informed decision-making for healthcare professionals.			

---

##  Repository Structure

```sh
└── medical_copilot/
    ├── README.md
    ├── assets
    │   ├── response-1.json
    │   ├── response-2.json
    │   ├── response-3.json
    │   └── response.json
    ├── backend
    │   ├── .DS_Store
    │   ├── README.md
    │   ├── case.py
    │   ├── db.py
    │   ├── llama_functions.py
    │   ├── main.py
    │   ├── requirements.txt
    │   └── test_main.py
    └── frontend
        ├── .eslintrc.json
        ├── .prettierrc
        ├── README.md
        ├── app
        │   ├── copytext.ts
        │   ├── dashboard
        │   │   ├── case
        │   │   │   └── [case_id]
        │   │   ├── layout.tsx
        │   │   ├── page.tsx
        │   │   └── upload-section.tsx
        │   ├── layout.tsx
        │   ├── page.tsx
        │   └── requests.ts
        ├── components
        │   ├── card
        │   │   └── index.tsx
        │   ├── case-status-tracker
        │   │   └── index.tsx
        │   ├── case-step-expander
        │   │   └── index.tsx
        │   ├── linear-loader
        │   │   ├── index.tsx
        │   │   └── styles.module.css
        │   ├── modal
        │   │   └── index.tsx
        │   ├── req-pill
        │   │   └── index.tsx
        │   ├── section-uploader
        │   │   └── index.tsx
        │   ├── spinner
        │   │   ├── index.tsx
        │   │   └── styles.module.css
        │   ├── submit-button
        │   │   └── index.tsx
        │   └── veneer
        │       └── index.tsx
        ├── context
        │   └── dashboard-context.tsx
        ├── next.config.js
        ├── package-lock.json
        ├── package.json
        ├── postcss.config.js
        ├── styles
        │   └── globals.css
        ├── tailwind.config.js
        ├── tsconfig.json
        └── utils
            └── index.ts
```

---

##  Modules

<details closed><summary>backend</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [main.py](https://github.com/jrp2212/medical_copilot/blob/master/backend/main.py)                       | This code establishes the main server logic for the medical_copilot application. It initializes the FastAPI framework, sets up CORS middleware, loads the Meta-Llama-3-8B-Instruct model on startup, and offers essential API routes. These routes facilitate creation of unique medical cases, retrieval of a specific case based on its ID, fetching of all cases with pagination, and listing of available server routes. Substantial exception handling is applied to maintain server reliability and integrity.                                                                        |
| [llama_functions.py](https://github.com/jrp2212/medical_copilot/blob/master/backend/llama_functions.py) | The given code snippet is part of the medical_copilot project's backend module. It includes functions responsible for loading a text generation transformer model, generating responses based on provided messages, and analyzing those responses. Primarily, these functions enable the system, acting as a medical assistant, to extract procedure names, CPT codes, medical record summaries, and appropriate options with reasoning from a given medical record and procedure guide. Additionally, there are functions to unload the model, optimizing memory usage of the application. |
| [case.py](https://github.com/jrp2212/medical_copilot/blob/master/backend/case.py)                       | The case.py module in the backend directory of the medical_copilot repository is responsible for creating and managing individual medical cases. It assigns a unique ID upon case creation, tracks progress, and maintains case-related information. This file uses different JSON responses based on case progress to provide information such as procedure name, CPT codes, and summary. Additionally, it performs error handling for exceptions arising from reading the JSON files.                                                                                                     |
| [db.py](https://github.com/jrp2212/medical_copilot/blob/master/backend/db.py)                           | The db.py file commands an in-memory database in the medical_copilot project's backend. It primarily stores records for efficient retrieval and provides pagination functionality for handling larger amounts of data effectively. The database also facilitates record addition, length measurement, and specific record querying by ID.                                                                                                                                                                                                                                                   |
| [test_main.py](https://github.com/jrp2212/medical_copilot/blob/master/backend/test_main.py)             | This code conducts unit tests on the main backend module of a Medical Co-Pilot application. It verifies functionalities such as creating medical cases, retrieving all case IDs, and fetching individual case details. It ensures correct status updates over time for a given case, validates responses from the server, and maintains uniqueness of the case ID as part of rigorous data integrity checks.                                                                                                                                                                                |
| [requirements.txt](https://github.com/jrp2212/medical_copilot/blob/master/backend/requirements.txt)     | This code is part of the backend section of the medical_copilot repository. The file requirements.txt lists the specific versions of Python libraries needed for the project. These libraries include FastAPI for building APIs, Uvicorn for ASGI server, HTTPX for Async Http requests, Pytest for testing, and others for various functionalities. Their correct installation is crucial for the smooth execution and integration of the application's backend.                                                                                                                           |

</details>

<details closed><summary>frontend</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [.eslintrc.json](https://github.com/jrp2212/medical_copilot/blob/master/frontend/.eslintrc.json)         | This code snippet is the ESLint configuration for the frontend of the medical_copilot repository, designed to enforce consistent code quality standards. It extends next/core-web-vitals, emphasizing Google's Web Vitals metrics, and sets a specified rule that React Hooks' dependency array need not be exhaustive. Part of maintaining the frontend's codebase, it's instrumental in optimizing web performance and ensuring smooth hooks usage. |
| [next.config.js](https://github.com/jrp2212/medical_copilot/blob/master/frontend/next.config.js)         | This code in next.config.js is critical for routing in the frontend of the Medical Copilot repository. It helps redirect paths starting with /dashboard/v6/prior-auth/upload/ to /dashboard/interqual-prior-auth/, a feature that supports dynamic changes of the repository's user interface based on specific user requests.                                                                                                                        |
| [tsconfig.json](https://github.com/jrp2212/medical_copilot/blob/master/frontend/tsconfig.json)           | The tsconfig.json in the frontend directory configures TypeScript compiler options for the Medical Copilot application. It sets up project-specific behaviors, including the JavaScript version used (ES6), module resolution style, and rules for handling JSX, aiming to maintain code quality and interoperability. Moreover, it sets specific path aliasing for cleaner imports and includes plugins to work with the Next.js framework.          |
| [postcss.config.js](https://github.com/jrp2212/medical_copilot/blob/master/frontend/postcss.config.js)   | The postcss.config.js file in the frontend directory configures post-CSS processing for the Medical Copilot project. It makes use of the Tailwind CSS and Autoprefixer plugins, to automatically manage the CSS utility classes and accommodate browser-specific CSS rules, respectively. This contributes to the consistent, responsive, and browser-compatible UI of the application.                                                               |
| [package.json](https://github.com/jrp2212/medical_copilot/blob/master/frontend/package.json)             | This package.json file houses configurations for the frontend of the Medical Copilot application using the Next.js framework. The scripts section includes commands for development, production build, and linting. Dependencies include UI libraries, design utility tools like TailwindCSS, HTTP client Axios, and unique id generation with uuid, while devDependencies cover TypeScript types and Sass for CSS pre-processing.                    |
| [tailwind.config.js](https://github.com/jrp2212/medical_copilot/blob/master/frontend/tailwind.config.js) | The tailwind.config.js file in the frontend directory tunes the Tailwind CSS framework settings for the Medical Copilot application. It determines the locations to remove unused styles, extends the color palette of the theme, particularly introducing a new pablo color scheme, thereby directing the overall aesthetics of the user interface in accordance with the application's design language.                                             |
| [package-lock.json](https://github.com/jrp2212/medical_copilot/blob/master/frontend/package-lock.json)   | This snippet represents the structure of a medical_copilot repository, built to facilitate health advisory. The backend handles data processing and logic execution, while the frontend manages user interactions. The assets folder stores JSON response files used by the application. Key operations are designed in main.py, llama_functions.py, db.py, and case.py in the backend.                                                               |

</details>

<details closed><summary>frontend.styles</summary>

| File                                                                                              | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---                                                                                               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [globals.css](https://github.com/jrp2212/medical_copilot/blob/master/frontend/styles/globals.css) | This code from the globals.css file in the frontend directory primarily configures global CSS styles for the Medical Copilot app. It orchestrates the aesthetics and behavior of various elements using Tailwind CSS and custom rules. Specifically, it customizes the scroll behavior, customizes accordion animations, and alters the style for different Material UI components. The code supports the application UI's overall integrity and ensures uniform styling across different application components. |

</details>

<details closed><summary>frontend.utils</summary>

| File                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [index.ts](https://github.com/jrp2212/medical_copilot/blob/master/frontend/utils/index.ts) | The index.ts code in the utils subdirectory of the frontend provides several functions that enhance the user interface's functionality. This includes simulating delays for asynchronous actions, cleansing URLs by removing superfluous slashes, extracting case IDs from URLs, and parsing case information to neatly structure data for clearer frontend processing. It supports the repository's mission by ensuring smooth information handling and user experience in the medical copilot application. |

</details>

<details closed><summary>frontend.components.veneer</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/veneer/index.tsx) | This code features a React component (`Veneer`) in the frontend of the `medical_copilot` repository. The component applies an overlay or veneer on its child components when the disabled prop is set. This not only visually masks the underlying elements but also blocks all mouse events, effectively rendering them non-interactive. It is beneficial for temporarily disabling user interactions on specific UI sections. |

</details>

<details closed><summary>frontend.components.case-step-expander</summary>

| File                                                                                                                 | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/case-step-expander/index.tsx) | This code represents the CaseStepExpander component in the frontend of the medical_copilot repository. The core function of this component is to display case step details, including a question and multiple options. It also provides a visual indication of whether the requirement step is met or not by using the CaseReqStatusPill component. Additionally, an accordion element is provided for additional explanatory notes or rationale. This component plays a critical role in user interaction within the medical case management process of the software. |

</details>

<details closed><summary>frontend.components.modal</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/modal/index.tsx) | This code comprises the Modal component, a critical part of the frontend architecture of the medical_copilot project. The Modal component is used for creating interactive dialog boxes or windows that overlay on top of the application's content. It possesses attributes that contribute to controlling its visibility, content delivery, size and optional close button feature. The code leverages the react-dom portal and framer-motion library for seamless animations and user interface experience. |

</details>

<details closed><summary>frontend.components.req-pill</summary>

| File                                                                                                       | Summary                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                        | ---                                                                                                                                                                                                                                                                                                                                                                   |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/req-pill/index.tsx) | This piece of code is a component for the Medical Copilot frontend. Specifically, it provides a Requirement Status Pill that displays whether a particular medical case requirement has been met or not. The visual feedback changes based on the boolean status, showing green for met requirements and red otherwise. The message displayed can also be customized. |

</details>

<details closed><summary>frontend.components.submit-button</summary>

| File                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/submit-button/index.tsx) | The SubmitButton component in the frontend of the medical_copilot repository triggers an asynchronous task when clicked. It provides visual feedback, showing a spinner during task execution and displaying success or error messages upon task completion. The component uses a finite state machine to manage its operation states. It includes a one-shot setting determining whether the button can be clicked multiple times or just once, and it reports completion status back to its parent. |

</details>

<details closed><summary>frontend.components.linear-loader</summary>

| File                                                                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                                                  |
| ---                                                                                                                             | ---                                                                                                                                                                                                                                                                                                                                                                                      |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/linear-loader/index.tsx)                 | The `LinearLoader` component in the `frontend/components/linear-loader/index.tsx` file of the `medical_copilot` repository presents a loading animation. It offers customizable styles and colors, enhancing user experience during data fetching or processing periods.                                                                                                                 |
| [styles.module.css](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/linear-loader/styles.module.css) | This CSS module applies styles to the Linear Loader component in the frontend of the Medical Copilot app. It defines two classes for loading animation in the application: loader, that sets up the container for the loader, and loaderfill, that animates a bar filling up the loader's width. This loader visually indicates that a task is ongoing, improving the user's experience. |

</details>

<details closed><summary>frontend.components.section-uploader</summary>

| File                                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                              |
| ---                                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                  |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/section-uploader/index.tsx) | This code from the SectionUploader component provides an interactive, customizable upload section mechanism for the Medical Copilot dashboard's frontend. It utilizes a Submit Button for performing asynchronous actions, alongside managing state changes. It aids the user in executing tasks and managing completion results, handling various interactive states indicated by different labels. |

</details>

<details closed><summary>frontend.components.case-status-tracker</summary>

| File                                                                                                                  | Summary                                                                       |
| ---                                                                                                                   | ---                                                                           |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/case-status-tracker/index.tsx) | |

</details>

<details closed><summary>frontend.components.card</summary>

| File                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                 |
| ---                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                     |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/card/index.tsx) | The `frontend/components/card/index.tsx` file creates a customizable Card component in the user interface of the Medical Copilot application. This reusable component, part of the frontend architecture, displays content wrapped within a consistently styled UI element, enhancing the overall visual cohesion across the application and reducing code duplication. |

</details>

<details closed><summary>frontend.components.spinner</summary>

| File                                                                                                                      | Summary                                                                   |
| ---                                                                                                                       | ---                                                                       |
| [index.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/spinner/index.tsx)                 |  |
| [styles.module.css](https://github.com/jrp2212/medical_copilot/blob/master/frontend/components/spinner/styles.module.css) |  |

</details>

<details closed><summary>frontend.context</summary>

| File                                                                                                                   | Summary                                                            |
| ---                                                                                                                    | ---                                                                |
| [dashboard-context.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/context/dashboard-context.tsx) | |

</details>

<details closed><summary>frontend.app</summary>

| File                                                                                           | Summary                                              |
| ---                                                                                            | ---                                                  |
| [requests.ts](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/requests.ts) | This typescript code The JavaScript defines two asynchronous functions using Axios for HTTP requests, designed to interact with an API for managing "cases". |
| [copytext.ts](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/copytext.ts) | `frontend/app/copytext.ts` |
| [page.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/page.tsx)       | `frontend/app/page.tsx`    |
| [layout.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/layout.tsx)   | `frontend/app/layout.tsx`  |

</details>

<details closed><summary>frontend.app.dashboard</summary>

| File                                                                                                                   | Summary                                                               |
| ---                                                                                                                    | ---                                                                   |
| [page.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/page.tsx)                     | `frontend/app/dashboard/page.tsx`           |
| [layout.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/layout.tsx)                 |  `frontend/app/dashboard/layout.tsx`         |
| [upload-section.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/upload-section.tsx) |  `frontend/app/dashboard/upload-section.tsx` |

</details>

<details closed><summary>frontend.app.dashboard.case.[case_id]</summary>

| File                                                                                                                              | Summary                                                                            |
| ---                                                                                                                               | ---                                                                                |
| [page.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/case/[case_id]/page.tsx)                 |  `frontend/app/dashboard/case/[case_id]/page.tsx`         |
| [case-error.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/case/[case_id]/case-error.tsx)     |  `frontend/app/dashboard/case/[case_id]/case-error.tsx`   |
| [case-section.tsx](https://github.com/jrp2212/medical_copilot/blob/master/frontend/app/dashboard/case/[case_id]/case-section.tsx) |  `frontend/app/dashboard/case/[case_id]/case-section.tsx` |

</details>

---

##  Getting Started


###  Installation & Setup

1. Clone the medical_copilot repository:

```sh
git clone https://github.com/jrp2212/medical_copilot
```

2. Change to the backend directory:

```sh
cd medical_copilot\backend
```

3. Install Requirements/Dependencies

```sh
pip install -r requirements.txt
```

4. Spin up FastAPI Server

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

5. Change to the frontend directory:

```sh
cd medical_copilot/frontend
```

6. Install the dependencies:

```sh
npm install
```

7. Adjust Line 4 of `frontend/app/requests.ts` to reflect the correct backend endpoint.


8. Spin up Client Server:

```sh
npm run dev
```

###  Tests

To execute tests, run:

```sh
npm test
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/jrp2212/medical_copilot/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/jrp2212/medical_copilot/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/jrp2212/medical_copilot/issues)**: Submit bugs found or log feature requests for Medical_copilot.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/jrp2212/medical_copilot
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---
