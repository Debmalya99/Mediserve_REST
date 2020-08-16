# Project Mediserve REST API

#### Smart disease predictions based on your symptoms

For more information check out the Mediserve Repository:
[Link to Mediserve repository](https://github.com/Debmalya99/Mediserve)

This is a REST API implementation of Mediserve project, which I did a few months ago as a part of Techno India Future proof hackathon. The main intention behind this rest API is to extend its functionality to other form of front ends like websites and apps.

#### Tha basic format of the API url : (I'll try adding more documentation later.)
* /api/mediserve/v1/[symptom]
where [symptom] is a long list of symptoms in json format given as:
{"symptom":[list of symptoms, which is 18 all times]} 

Of course not all the time all symptoms are needed, so default values will mostly be set to 'not_needed'. A detailed list will be provided later.
