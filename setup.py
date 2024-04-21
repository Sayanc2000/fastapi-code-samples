from setuptools import setup

long_description = """"
# Docs Sample Code

"""

setup(
    name="fastapi_code_samples",
    packages=['fastapi_code_samples'],
    version="0.0.1",
    author="Sayan Chakraborty",
    author_email="sayanc20002@gmail.com",
    description="Sample code generator for FastAPI OpenAPI schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sayanc2000/fastapi-code-samples",
    include_package_data=True,
    install_requires=['fastapi'],
    license='MIT License',
    keywords=[
        'redoc', 'openapi', 'swagger', 'fastapi'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.9',
)
