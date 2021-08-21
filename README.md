Project CookingMonster
Django REST framework app

Recipes book application where users can create profile, view recipes from other users.
Unauthenticated users can only view recipes.

URLs:
http://127.0.0.1:8000/admin/ - admin site
http://127.0.0.1:8000/ - index - not created yet - GET
http://127.0.0.1:8000/recipes/ - list all recipes - GET, POST(for authenticated users)
http://127.0.0.1:8000/recipes/<int:pk> - recipe detatils - GET, POST, PUT, PATCH, DELETE(for authenticated users)
http://127.0.0.1:8000/recipes/<int:pk>/comments/ - comments GET, POST
http://127.0.0.1:8000/accounts/register - register new user POST
http://127.0.0.1:8000/accounts/login/ = login with JWT POST
http://127.0.0.1:8000/accounts/login/refresh/ refresh login token POST
http://127.0.0.1:8000/accounts/logout/ - logout  with JWT - blacklist token POST
http://127.0.0.1:8000/accounts/change_password/<int:pk> - user change password - for owners only POST
http://127.0.0.1:8000/accounts/update_profile/<int:pk> - update user profile POST




