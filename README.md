# The Recipe App

### Introduction
![image](https://user-images.githubusercontent.com/31623888/226194939-7b2bc815-02ce-4ad4-b77e-396e23713403.png)

This recipe web application is based on Django framework, and which includes two apps: users app and recipes app. The backend is built by Python, and the frontend pages are built by html. This app enables users to view recipes, search recipes by keyword, upload their recipes, edit/view/delete of their uploaded recipes. A registered user is required for uploading and modifying recipes. Search recipe function can be used without registration. The attached screenshot is how the website looks like. It can support main demandings from our potential users. Though I've set up some settings on Heroku, I didn't deploy it to a remote server in the end because it's not free any more even if it's for a personal project.

### Follow the steps to go through all functions
#### Search for a recipe
Our web users can simply input the recipe keyword and click the "Search" button to search for a recipe. If the keyword doesn't match to an existing recipe, then the page will return "recipe not found". 

#### Register and Login
![image](https://user-images.githubusercontent.com/31623888/226204203-a70f4199-ee54-4c85-a9f5-92126cf8b838.png)

![image](https://user-images.githubusercontent.com/31623888/226204235-fab2516e-50ca-43cb-a0ec-a96b8cd88cb4.png)

Click the "register" button to create a new account or click the "login" button to log into your account. After logging into your account, you are free to use the following functions now.

#### Upload your recipe
![image](https://user-images.githubusercontent.com/31623888/226201062-92584f7d-9468-47a8-8526-ada7fd5b7826.png)

After logged into your account, then you can click "Upload my recipe" and fill in the form. As the form is successfully submitted, you should be able to see your recipe on the home page. 

#### View and modify your recipes
![image](https://user-images.githubusercontent.com/31623888/226201039-6a65ae9e-779c-42dd-9a07-0884ea6b26fd.png)

Clicking "My recipes" button, you will see a table that list the brief information of each recipe. You can delete or modify or view the details of the recipe by clicking the buttons on the right hand side of each recipe. 

#### Log out
Feel free to log out your account by clicking the logout button on the navigator bar.

#### Unit Tests
I've added unit tests for both recipes app and users app under the tests folder.

#### Integration Test

![image](https://user-images.githubusercontent.com/31623888/226202500-466b6456-9aab-4c0e-9c45-7b6e53d80357.png)

The integeration test was generated at recipe_platform/htmlcov/index.html

### Future steps
I would like to apply AWS rather than the Django default database to store more data. I also hope to deploy this app to a remote server so that it can be used by the public.

### References
https://docs.djangoproject.com/en/4.1/            
https://blog.getbootstrap.com/2021/05/05/bootstrap-5/        
https://www.educative.io/courses/django-takeoff-develop-modern-apps     
https://www.modernhoney.com/chinese-orange-chicken/       
https://tastesbetterfromscratch.com/easy-tiramisu/       
https://www.eatwell101.com/garlic-butter-steak-and-potatoes-recipe          
https://www.thewholesomedish.com/the-best-homemade-tacos/       

