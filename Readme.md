# Snippet Lister

## What's that ?!
Hi !
This is a small plugin that allow you to open and edit your sublime snippet *from* Sublime.

## Download

The best way to download this Sublime's plugin, it's of course to do it from [Package Control](https://packagecontrol.io/installation)

Else, you can download the code on [Github](http://github.com/math2001/snippet-lister), and extract it in the `Packages` folder.

## Config

For this plugin work the best, you need to respect logic "rules":

1. Put *all* you snippet in the the `User` folder, and then, in a folder with the name of your choice. For exemple, `snippet`
2. Inside this last folder, create one folder *per* langage, with the name of the langage. For exemple `python`.

Remember the custom folder name ? You need to report it in the `Settings - User` file, like this :

```
"main_snippet_folder_name": "your_custom_folder_name"
```

*And that's it!*

If you don't do this, the plugin will still working, but not the best way it can.



## Navigate in your folder

If you have folder inside the deepest snippet's folder, no worry, you still can go into it, just select it !
Also, you can go in the parent folder by selecting the `..`

## Understand how it's work

The concept is realy easy to understand :

I have a list with all the folder the plugin must go. It look like this :

```
["Packages", "User", "your_custom_folder_name", "the name of the current langage"]
```

For each folder, it try to go inside, but if it can't, it still try the following ones, it just skip it.

> So, what end ?

It's mean that you can skip one folder if you want to.

### The name of the langage

The plugin know the name of the langage by selecting the name of the `.sublime-syntax` (in ST3) file.

*Hope you enjoy it!*