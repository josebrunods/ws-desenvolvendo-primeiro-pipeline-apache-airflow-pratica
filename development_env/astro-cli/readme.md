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

Now where we going to access some files for our data pipeline

Let's access our internal data lake:

```sh
# minio
access_key: workshop_airflow
secret_key: w0rks6p@1rfl0
```

This data lake we will have access to our landing files, these files are fake for testing and development purpose, we will use for our data pipelines and lab.


*Be mindful that the main idea is to deliver a closer look in real-life problems, we mimic the data but it is a mimic, data is not always clean as we desire.*