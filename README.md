# delete_by

## Description
This project is built in python and it enables the user to free up disk space in one of their elasticsearch clusters (defined in the config.py file w/in the modules directory) based on a query that will look for the presence of specific documents and if those documents exist they will be deleted from the index using a delete_by query. Once, the delete_by query has finished all of the related documents will have been deleted, but they are still associated with the index until the index is merged. I believe it is an option to wait for the cluster to merge the index on its own, but that seems to take a while. The second part of this project is running a force_merge function on the index that has just had the delete_by query run on it. The force_merge will permanently remove all of the deleted docs which will actually free up the disk space to reduce the total amount of disk space the affected index requires.

This is also my first attempt to make a modular application. I will be taking the lessons learned here to make a larger repository to be used on a larger script that has multiple different types of functionality and reporting. The goal is to combine all of the python functions that have been developed into one application that will allow a more automated approach to some of the issues that we have been coming across or allow us a more efficient troubleshooting process when we run into unknown issues.

## Usage
As the syntax reads at this time there is a hard coded delete_by query in place as well as a hard coded alias. These are two areas of improvement that would allow this project to be more dynamic. At this point this query is making a list of all indices in the filebeat alias and then checking them for the presence of two fields within filebeat docs and if they exist with the listed values the index will move on to the next stage of the application which is the delete_by query and then on to the force_merge. Before using this application be sure you have validated that you have the proper query that you are looking for to ensure that you get rid of the right data.

## Roadmap
I might try to make the query and alias process more dynamic, but the main point of this project was to help me figure out how to create an application and organize it properly so it is easy to continue to make additions to.
