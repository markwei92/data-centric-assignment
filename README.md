1) Data Centric Cookbook Project

-Project Goal

This is an online cookbook mobile web app that allow all users to add their own cooking recipes as a contribution to the community. 
Therefore no login is required as users are expected to be respectful of one another's contribution; not to edit or delete without the author's permission. 

The main goal of this project is to get everyone to contribute back to society by showcasing each other's food culture and heritage, due to geographical differences it can be difficult to have access to these cruisines. Therefore I created this web app to allow users to share their food expertise and cruisine online so that users all around the globe can have a chance to try cooking from these various recipes.


2) UX

-Strategy

My strategy for the UX design was to create filters to allow easy sorting based on categories. The UX design is fairly simple and straightforward to use, the main page displays all the recipes and there are filters at the navbar whereby they can search based on category to whip up something simple or challenging.

-Navigation

<Logo>
When loading up the front page, you will be greeted with a white screen with a nice logo which says 'Delicious Food Blog'. This logo icon when clicked will bring you back to the home page which we are currently viewing.

<Search Filters Overview>
On the home page we have the row of filters on the top right in which there is a large caption in teal stating search filters. Below the search filters are 5 different filters which you can click on to brin you the selected filter page, 'Food Origins', 'Dish Type', 'Dietary Requirements', 'Difficulty Level' and 'Multi-Criteria'. I will explain more in detail later on.

<Adding New Recipe>
Moving along down the home page, at the top left corner just below the logo icon there is an 'add new recipe' button in green. For users who wish to add new recipes, simply click on it and it will bring you to the add recipe page. In the add recipe page there is the title at the top which the user inputs the title of the dish, followed by the author AKA the user or the person who invented this dish, next we have the ingredients list as shown with a large textbox to key in all the ingredients.

The final 4 below the instructions textbox are the specific category filters in which the users choose the appropriate category which will also in turn be used later on to filter recipes based on the different search filters as mentioned earlier in the homepage. After all of the filters have been selected, user will scroll to the bottom of the page and hit the submit button to save, this will store the all the information the user has written into the mongoDB database. The page will refresh and reroute the user back to homepage.

<Viewing Recipes>
At the homepage below the add recipe button, we will be able to see all the recipes from the database including the ones the user has just created. Each recipe displays 3 basic information, the title, the food origins and the type of cruisine. If users are interested to find out more about this recipe they can click on the view recipe button just below to see the full recipe.

<Editing & Deleting Recipes>
This will route them to that specific recipe page detailing all the information that was keyed in by the author when he/she added a recipe in the add recipe page. At the bottom the user will see edit, delete and return to previous page buttons. The edit button will allow the user to edit the recipe routing them to a page like the add recipe page, just that now there will be information inside instead of blanks. Users can make any amendments and hit the save button or they can cancel to revert back to original, both when clicked will route the user back to the homepage. The delete button basically just removes the recipe from the database, there will be a prompt asking whether they are certain whether the user wants to remove it by clicking a yes or no button. Thereafter the user will be routed once again back to the homepage. As for the return to previous page button, it does not automatically bring you back to the homepage, rather as the name states, it brings you back to the page before, so let's say if the user was on one of the search filters page, the user will be routed back to that page with all the search results still intact.

<Search Filters Indepth>
 
Now we move onto the search filters page, each filters performs very similarly in which the user clicks on one of the search filters in on the top right of the web app and this will route them to the filter page, whereby there will be one specific filter or many depending on the search filter chosen. Let's say the user chooses the food origins search filter, he clicks on it and it brings him to the filter page, from there the user will see a gray box, by clicking on the box there will be a dropdown that will show all the categories available for this filter. Say the user chose the Chinese filter, he selects it and clicks submit, the page will load and there should be one search result called Chinese Pepper Steak. And likewise the user can view the recipe all explore the other search filters. If there are no results for particular filter, that means that there isn't any recipe that is contained within this category of recipe.

All the filters work the same way except for the last filter on the right which says multi-criteria. This filter when clicked allows the user to filter by a selection of more than one criteria. This is especially good if the user wants to refine down to a very specific filter. The user however has to ensure all the filters are selected and cannot be left blank, otherwise when hitting the submit button, the app will display an error message. This wraps up how to navigate through the web app, if the user wishes to return to the homepage, he does not need to use the back button, rather he can just click on the logo icon on the top right to return back to all recipe where the user can view all the recipes or add recipes. For editing and deleting of recipes, the user can only perform those 2 functions when they are in the recipe view.


3) Limitations

<Bullet points and numbering for add new recipe page>

In the add recipe page the user will have to input their own numbering or bullet points as I did not have any segregation within the textbox, this is a limitation I'm working on as I have not found a suitable method to do it. Likewise for the instructions textbox below the ingredients textbox, users have to manually fill up all the details on how to cook the dish and the specific steps to take and the things to look out for when preparing this dish.
 
<Pagination on homepage for all recipe display>

In the homepage, I struggled to get the pagination to load properly when displaying all recipe, which results in the homepage being very lengthy when more recipes are being added in. Reason I struggled was because many of the pagination resources are more focused on mySQL and does not have examples on linking the pagination with the MongoDB database, I have tried several methods but none have proven successful.

<Selective filtering when using the Multi-criteria filter>

Under the Multi-Criteria filter I was not able to do selective filtering, meaning that I had to pick all the filters for it to work and leaving any filters unselected will bring up an error. I am not able to pinpoint the code causing this error and as such I was not able to do selective filtering, but rather all the filters must be chosen for it to work.

<String search as a search filter>

I was not able to input a text string search which I felt would be helpful to the user who already know what they were looking for, but given the limited resources available for MongoDB frontend integration and the difficulty of implementation and adaptation from various stackoverflow resources I could only do filter selection.


4) Features

I used simple category search filters as it is relatively straightforward and users can narrow in what they want through the search.
Thereafter they can select the view recipe button to get a full loadout on the recipe.
If its not to their liking the user can return back to search or choose a different search category.
Users can also contribute by adding new recipes in the homepage and they can proceed to edit or delete the recipe in the view receipe page later on if necessary.


5) Frameworks Used

The project uses Flask framework and mongoDB database to store and integrate data with the frontend development. Programming languages for the frontend display of the web app cookbook includes HTML, CSS, Javascript and for the backend development Python is used.


6) App Testing

For testing this web application, I did manual testing, I first tested the CRUD (Create, Read, Update, Delete) functions ensuring that the every update and creation is saved and properly reflected on the homepage as well as the search filters. To do this, in the homepage I first clicked on the add recipe button to ensure I was able to create a recipe, this will bring me to the add recipe page, whereby I will fill up all the information that is required of the user and hit the submit button, this will reroute me back to the main page. Scrolling through the main page I was able to find my newly added recipe. Next I tested the cancel button in the add recipe page, the result was that it brought me back to the homepage but this time without the recipe being saved into the database.

<View Recipe, Edit & Delete Buttons Testing>

Next I tested the view recipe button for one of the recipes, this will bring me to the corresponding recipe page that details down all the information about this recipe. I clicked on the edit button and made a change to each filter and textbox, the changes were saved using the save button and the recipe was updated properly in the homepage. Next I tested the delete button, which pops up a yes and no button, if I clicked yes, the recipe entry will be taken off the database, if I clicked no it will remain as it is and bring me back to the homepage. Lastly I tested the return to previous page button first, by viewing recipe through search filters, when I clicked on the previous page button it will bring me back to the search filter instead of the homepage.

<Search Filters Testing>

Next I tested the filter tabs by clicking on every individual filter to ensure that all of them is working as intended. For the first search filter located on the top I clicked on food origins which will route me to the food origins filter page, next I clicked on the Chinese, Malay, Indian and English tabs followed by the submit button to ensure each of them has their correct corresponding results by comparing them with the home page under all recipe to ensure that only recipes pertaining to that selected filter showed up. The last filter, the multi-criteria filter due to limitations can only perform the search if all the filters are selected, if one or more is excluded an error will display, likewise the results are compared with all recipes in the homepage to ensure the filters corresponded to every individual filter.

7) Bugs Solved

<Getting the database to link correctly with the html>

Getting the data to be retrieved onto the ubuntu terminal was a simple task as it was taught in the code institute videos, however getting that same information displayed on the front end using html was more challenging and it took me many days to get the code working not only retrieving the data but also displaying them correctly in the desired format. Definitely a big accomplishment for me considering there were very little relevant materials on the web that provided information on how to do front end integration with MongoDB using the filter search. Alot of trial and error as well as adaptation based on other contributors solution.

<Getting the view recipe page to load correctly>
 
The view recipe page basically loads up all the information about the recipe, user uses the search filter function to find recipes, when first displayed it is in a basic form showing title, food origin and cruisine type. By clicking on the view recipe button below, it will bring the user to the view the entire recipe. This was not taught by code institute, therefore I had to do alot of improvisation looking at my code on editing recipe, using it to create a new set of code that will display the data of the recipe accordingly like how it would display when clicking the edit recipe button but this time without the ability to make amendments, but only for viewing purposes. This was also a challenging process but after several rounds of iteration, I finally managed to crack the code and have it work smoothly.

8) Deployment

Deployed using Github for repository and documentation, for web app deployment I used Heroku for server hosting, hosting is relatively straightforward and quick to setup and connect. Followed the heroku hosting steps given on the code institute tutorial, very straightforward and easy to deploy.


9) Technologies Used

For this project, I am using the MongoDB Database in conjunction with python to store recipe information and also to be used for information retrieval later on.

For the backend integration with frontend I am using Jinja and Flask to connect the MongoDB database to the html and web display.

For the frontend development I used HTML, CSS and Javascript derived using a template from colorlib.


10) Acknowledgement & Media

-I received inspiration for this project from code institute on the online cookbook suggestion.
-Website layout taken from Colorlib: https://colorlib.com/wp/template/delicious/

Recipe info and contents taken from allrecipes website:

1) https://www.allrecipes.com/recipe/232337/kims-lasagna/?internalSource=streams&referringId=502&referringContentType=Recipe%20Hub&clickId=st_trending_b
2) https://www.allrecipes.com/recipe/172704/chinese-pepper-steak/?internalSource=streams&referringId=695&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
3) https://www.allrecipes.com/recipe/228293/curry-stand-chicken-tikka-masala-sauce/?internalSource=streams&referringId=17136&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
4) https://www.allrecipes.com/recipe/78938/malaysian-nasi-lemak/
5) https://www.allrecipes.com/recipe/229156/zesty-quinoa-salad/?internalSource=streams&referringId=87&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
6) https://www.allrecipes.com/recipe/71003/coconut-cream-pound-cake/?internalSource=streams&referringId=79&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
7) https://www.allrecipes.com/recipe/61913/authentic-chinese-egg-rolls-from-a-chinese-person/?internalSource=streams&referringId=113&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
8) https://www.allrecipes.com/recipe/189352/indian-spiced-roasted-chickpeas/?internalSource=streams&referringId=1874&referringContentType=Recipe%20Hub&clickId=st_recipes_mades
9) https://www.allrecipes.com/recipe/112239/caramel-macchiato-cheesecake/?internalSource=hub%20recipe&referringContentType=Search


