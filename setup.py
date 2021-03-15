# SPDX-License-Identifier: GPL-3.0-or-later
from setuptools import setup, find_packages


setup(
    name="cachito",
    version="1.0",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "celery<6",
        "gitpython",
        "kombu<5",  # A celery dependency but it's directly imported
        "packaging",
        "pyarn",
        "requests_kerberos",
        "requests",
        "semver",
        "setuptools",
    ],
    extras_require={
        "web": [
            "Flask",
            "flask-login",
            "Flask-Migrate",
            "Flask-SQLAlchemy",
            "psycopg2-binary",
        ],
    },
    entry_points={
        "console_scripts": [
            "cachito=cachito.web.manage:cli",
            "cachito-cleanup=cachito.workers.cleanup_job:main",
            "cachito-update-nexus-scripts=cachito.workers.nexus:create_or_update_scripts",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="GPLv3+",
    python_requires=">=3.6",
)
