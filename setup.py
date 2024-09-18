from setuptools import setup, find_packages

setup(
    name="prompt_hub_py",  # The name of your project
    version="0.0.1",  # Initial version
    author="Ashok Reddy",
    author_email="kummethashokumareddy@example.com",
    description="A package to manage prompts with PostgreSQL",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PromptMania/prompt-hub-py",  # Optional, if you have a GitHub repo
    packages=find_packages(),
    install_requires=[
        "psycopg2>=2.9.9",  # PostgreSQL adapter for Python
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
