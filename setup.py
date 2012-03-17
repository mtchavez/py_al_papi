import al_papi
from distutils.core import setup
setup(
    name="al_papi",
    version=al_papi.version.Version,
    description="AuthorityLabs",
    author="Chavez",
    author_email="support@authoritylabs.com",
    url="http://www.api.authoritylabs.com",
    packages=["al_papi"],
    package_data={},
    install_requires=[],
    tests_require=["nose", "pinocchio=0.3"],
    zip_safe=False
)
