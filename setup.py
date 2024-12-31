from setuptools import setup, find_packages

setup(
    name="create_agents",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer",
        "pyyaml",
        "jinja2",
    ],
    entry_points={
        "console_scripts": [
            "create-agents=create_agents.cli:app",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for scaffolding agent-based projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/create_agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
