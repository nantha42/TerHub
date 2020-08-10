# TerHub

### About
Helps to create and delete repository from command line.
Get an `personal access token` from your github developer settings.
Copy paste that token in `tokens.dat` in the main.py directory.
And create a `users.dat` in the same directory containing only your username(required for deleting repository).

```
TerHub
  |-main.py
  |-tokens.dat
  |-users.dat
```

To create a repository
```
python3 main.py -c --name Sample --private false 
```

To delete a repository 
```
python3 main.py -d --name Sample
```
