<div align="center">
<h1 align="center">
<img src="https://cdn-icons-png.flaticon.com/512/8001/8001997.png" width="100" />
<br></h1>
<h3>◦ RPA Projektarbeit Gruppe 2</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/XAML-0C54C2.svg?style=flat-square&logo=XAML&logoColor=white" alt="XAML" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON" />
</p>
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🎞️ Demo](#️-demo)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#️-modules)
- [🚀 Getting Started](#-getting-started)
  - [🔧 Installation](#-installation)
- [🛣 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
  - [Contributing Guidelines](#contributing-guidelines)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

This project is the Semesterwork of the CDS-309 Robotic Process Automation (RPA) Course in 2024. 

The project focuses on developing a RPA system to automate the extraction of data from invoice documents uploaded to a company's [website](https://rpa-project.maechler-thomas.ch/) (in this case it is a small fake website made for the course by the Prof.). The primary goal is to streamline the data extraction process, organizing the extracted data into an Excel file and sending it via email to the relevant user in the sales department.

Each day, various invoice documents are uploaded to the company's website by 8 AM. The RPA system should navigate the website, download all available documents, and perform data extraction to retrieve specific details such as invoice number, name, amount, company name, and address. This information should be formatted into an Excel file, which is then emailed to the user. The system must provide clear notifications of the process's success and allow for both automatic and manual initiation of the extraction process.

---

## 🎞️ Demo

The [Demo.mp4](Demo.mp4) is a 200mb 2 minute long video, with how it works (no sound is on purpose).

## 📦 Features

- **Automatic Navigation and Download**: The system should automatically navigate to `Main.html`, select "Rechnungen," and download all available documents (as well as go to `Weitere Rechnungen` and download all available files from there as well).
- **Data Extraction**: Extract the following information from invoice documents:
  - Invoice Number
  - First Name
  - Last Name
  - Amount
  - Company Name
  - Address
- **IKAVA DataService**: Use the IKAVA Dataservice to manage the data.
- **Excel File Generation**: Organize the extracted data into a daily Excel file.
- **Email Notification**: Send the Excel file via email to the user in the sales department.
- **Process Notifications**: Provide clear notifications upon successful completion of the process.
- **Manual Trigger**: Allow the user to manually trigger the process.
- **Data Organization**: Ensure the data in the Excel file is properly structured and readable.
- **Email Integration**: Automatically prepare and send an email with the Excel file attached.


---


## 📂 Repository Structure

```sh
└── /
    ├── BlankProcess/
    │   ├── .entities/
    │   ├── .local/
    │   │   ├── AllDependencies.json
    │   │   ├── BlankProcess.nuget.props
    │   │   ├── db/
    │   │   ├── install/
    │   │   ├── PackageBindingsMetadata.json
    │   │   ├── PackageCache.json
    │   │   ├── ProjectSettings.json
    │   │   └── RPA_Projektarbeit.nuget.props
    │   ├── .objects/
    │   │   ├── .metadata
    │   │   └── .type
    │   ├── .screenshots/
    │   ├── .settings/
    │   │   ├── Debug/
    │   │   ├── Design/
    │   │   └── Release/
    │   ├── .templates/
    │   ├── .tmh/
    │   │   └── config.json
    │   ├── bindings.json
    │   ├── CreateFolder.xaml
    │   ├── DownloadAllFilesFromWebsite.xaml
    │   ├── DownloadFiles.xaml
    │   ├── InteractionWithAI.xaml
    │   ├── Main.xaml
    │   ├── MakeLogFolderAndFile.xaml
    │   ├── project.json
    │   ├── scripts/
    │   │   └── extract_features.py
    │   └── WriteLog.xaml

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                            | Summary       |
| ---                                             | ---           |
| [RPAInvoiceCollector]({packages\RPAInvoiceCollector.0.0.4.json}) | The DataBase Invoice from IKAVA |
| [RPA Finished Package]({packages\RPA_Projektarbeit_Gruppe_2.1.0.1.nupkg}) | The Exported and compiled package with the whole bot in it. |
| [CreateFolder]({BlankProcess\CreateFolder.xaml}) | Workflow to create a new Folder |
| [DownloadAllFiles (from Website)]({BlankProcess\DownloadAllFilesFromWebsite.xaml}) | Workflow which clicks through all pages |
| [DownloadFiles]({BlankProcess\DownloadFiles.xaml}) | Workflow which downloads all Files on the pages |
| [MakeLogFolderAndFile]({BlankProcess\MakeLogFolderAndFile.xaml}) | Workflow to create the Logfiles |
| [WriteLog]({BlankProcess\WriteLog.xaml}) | Workflow to easily write into the Logfile |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ requirements.txt for Python (3.9)`

`- ℹ️ UIPath.WebAPI.Activities = 1.18.0`

`- ℹ️ UIPath.Python.Activities = 1.8.0`

`- ℹ️ UIPath.PDF.Activities = 3.16.0`

`- ℹ️ UIPath.Excel.Activities = 2.22.3`

`- ℹ️ UIPath.Mail.Activities = 1.12.3`


### 🔧 Installation

1. Clone the  repository:
```sh
git clone git@github.com:schneialexan/rpa-project.git
```

2. Open the Project in UIPath

3. Install local OLLAMA https://ollama.com/download and run the installer

4. Run the download for LLAMA3:
```sh
ollama pull llama3
```

5. Run the Server/Listener:
```sh
ollama serve
```

6. Setup IKAVA and the Invoice (see packages > RPAInvoiceCollector.0.0.4.json)

7. Setup all Packages/Dependencies in UIPath (WebAPI, PDF, Python)
   
8. Done!

---


## 🛣 Project Roadmap

> - [X] `ℹ️  Task 1: Implemented Feature Extraction with local LLAMA3`
> - [ ] `ℹ️  Task 2: Make code more readable`


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/local//blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/local//discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/local//issues)**: Submit bugs found or log feature requests for LOCAL.

### Contributing Guidelines

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone git@github.com:schneialexan/rpa-project.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
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

## 📄 License


This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/) License. For more details, refer to the [LICENSE](LICENSE) file.

---

## 👏 Acknowledgments

- Christian Gilomen (co-programmer)

[**Return**](#Top)

---

