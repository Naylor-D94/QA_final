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