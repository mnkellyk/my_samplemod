# my_samplemod
My hot take on how to structure a Python project.  Creates the entire structure of project, packages, and modules, including docs and tests artifacts.  Also evolved a bit to suit developments in standards, and finally adapted with some quality of life/ease of use standards.  

Which is all to say:
* All the files where they belong, even if they aren't implemented up-front.
* yaml file for CI/CD workflow under .github
* aggressive .gitignore to weed out the junk I don't want. 
* choice of mkdocs with material for documentation. Placheholder for mkdocs yaml file and docs/index.md.  Tree outline shows location of /site directory but that's in .gitignore so shouldn't be pushed.  Use __mkdocs gh-deploy__ for docs hosting.   I'm not a fan of Sphinx and I far prefer  MD instead of RST.
* Directory structure to support imports that work out of the gate.  Do not add any additional __init__.py files or do anything fancy with classpath or os.path, etc.  It's not necessary.  DO fully  qualified import statements like: __from my_sample.module_file1 import MyClass__
* implemented .env file with .env.example.dev as template.  DO NOT import .env into github.  It's included in .gitignore, put I put a placeholder here to show where it would go.  

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
