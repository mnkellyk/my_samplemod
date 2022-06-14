# my_samplemod
My hot take on how to structure a Python project.  Creates the entire structure of project, packages, and modules, including docs and tests artifacts.  Also eveloved a bit to suit developments in standards, and finally adapted with some quality of life/ease of use standfards.  

Which is all to say:

```
.
├── .github
│   └── workflows
│       └── python-app-wf.yml
├── my_sample
│   ├── docs
│   │   └── index.md
│   ├── logs
│   │   └── app.out
│   ├── my_sample
│   │   ├── __init__.py
│   │   ├── module_file1.py
│   │   └── module_file2.py
│   ├── site
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_module_file1.py
│   │   └── test_module_file2.py
│   ├── .env
│   ├── .env.example.dev
│   ├── __init__.py
│   └── mkdocs.yml
├── .gitignore
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── setup.py
└── todo.md

8 directories, 23 files
```
