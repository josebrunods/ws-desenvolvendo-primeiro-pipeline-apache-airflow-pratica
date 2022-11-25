# Workshop ~ Develop your first pipeline using Apache Airflow HandsOn ~ Astro CLI

## Setting you apache airflow dev env


To install Astro CLI, please follow the link below from official documentation

Install Astro CLI:
https://github.com/astronomer/astro-cli

* *Docker Desktop is needed for setup the env*

Let's start with simple command line to setup our development environment, first access your project folder in your local machine, then execute the commands:

```sh
# create project 
astro dev init

# start the compenents
astro dev start
```

After setup astro CLI he will open a Apache Airflow Webserver in your browser.

```sh
Login: admin
Password: admin
```

After the initialize the airflow environment, let's customize our changes move the content of the folder astro-cli/demo_dags to astrp-cli/lab/dags.

After this copy this content to requirements.txt in lab folder.

```sh
# <https://pypi.org/search/?q=apache-airflow-providers&o=>
apache-airflow-providers-microsoft-azure==4.3.0
apache-airflow-providers-microsoft-mssql==3.2.1
apache-airflow-providers-postgres==5.2.2
apache-airflow-providers-cncf-kubernetes==4.4.0
apache-airflow-providers-databricks==3.3.0
apache-airflow-providers-snowflake==3.3.0

# <https://pypi.org/project/astronomer-providers/>
astronomer-providers==1.10.0

# <https://pypi.org/project/minio/>
minio==7.1.12
```


After copy the files and content let's restart our astro cli project:

```sh
astro dev restart
```


Now where we going to access some files for our data pipeline

Let's access our internal data lake:

```sh
# minio
access_key: workshop_airflow
secret_key: w0rks6p@1rfl0
```

This data lake we will have access to our landing files, these files are fake for testing and development purpose, we will use for our data pipelines and lab.


*Be mindful that the main idea is to deliver a closer look in real-life problems, we mimic the data but it is a mimic, data is not always clean as we desire.*