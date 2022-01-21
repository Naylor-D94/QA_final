My app is a basic website to look at the information relating to certain newspapers.
It has links to their websites as well as lists their "fictional" editors.
My app fulfills the brief as it utilises the aspects requested, it is made with flask as the back and HTML as the front end using templates.
It is all Dockerized and has full functionality of CRUD using MySQl.
The ed.id in editors has a one to many relationship with the ed_id in the newspapers table.



My app works, by Selecting and showing the details of the newspaper table on the index page, showing the R in CRUD. It has HTMl links
to other functions in my app.py file, it links to an "add editor" function, which utilises form requests so the user can input a new editor into the db. Demonstrating C.
There is a link to the /update page, which allows the user to input the first name and last name of an editor, and then input an update to the date started column
in the database. The function checks that the first name and last name match with the users input and the updates date started as requested. Demonstrating U.
There is also a Delete link, which alllows the user to input the information for an editor and remove it entirely from the database. Demonstrating D.
C.R.U.D

Added unit tests to check for addition, multiplication, and capitalisation. As far as my knowledge goes on that subject as we were'nt shown in detail.
In future I probably won't make many changes to this file, but will keep it as a point of reference as I keep working on my other projects.

I have then setup Jenkins, allowing Jenkins user access to Docker, then Jenkins clones the repo, runs a script for docker-compose up to build the containers,
then moves on to the test stage to run the test_app.py with pytest.
It is linked to Giuhub push actions via a webhookrelay to activate the webhook on a local machine. Running this command will connect the localmachine to my relay
with my credentials.

relay login -k 4371b82d-8c80-49be-a9b6-71acc4d9724c -s fHoHxXtWkImf

The Jenkins pipeline has no deployment stage, as we never covered Docker swarm on the course due to time constraints and this is the requested deployment method.

Video link to demonstration : 
https://drive.google.com/file/d/1u5cMg_cuBQEBhQkQGT3FMKD3oLZyJHej/view?usp=sharing

Video displays full CRUD functionality on the app. Hosted in Docker alone due to the Jenkins file having a close function, then hosted on Jenkins to demonstrate 
that the pipeline works as expected. Followed by a view at the Jenkins code.