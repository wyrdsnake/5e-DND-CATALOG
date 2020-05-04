# 5e-DND-CATALOG

## Purpose
A discord bot for the purpose of sharing PHB races and classes over discord. Planning on adding spells, backgrounds, and equipment in 
later updates, as well allowing users to create, upload, and access their own homebrew creations.

Have you ever started a game of DnD online over discord, and have had literally no clue what you are doing? Per chance, have you
gotten into a spat with your DM about how the Rogue's sneak attack feature works (THEY DON'T NEED ADVANTAGE, JOE, IF AN ALLY IS WITHIN
FIVE FEET OF THE ENEMY IN QUESTION!)? Need a good place to store homebrew and share it with others? Look no further! The 5e DnD Catalog
seeks to solve all these problems!

Features:
- Using Web scraping through Python to pull information off of Roll20 with a command
  - For instance, !race kobold would bring up the Kobold race stats
  - Races with subraces, like an elf, would present the player with all possible options for elves, for them to choose from.
  (i.e. High elf, woof elf, drow, sea elf, etc)
  - This will also be used for classes and weapons, and spells, magic items, and backgrounds will be added in later updates.
  - putting in a command for a class (i.e. !class paladin) would show the quick build, progression table, and subclasses for that class. If a class has spellcasting, for now, it will bring them to the Roll20 spell search list with the given class as a filter.                   i.e. https://roll20.net/compendium/dnd5e/Spells%20List?sort=Level&amp;Classes[]=Paladin#content

## Use 

Invoke [name of bot] by typing `?dnd` followed by the command you wish to use.

## Commands 

N.B. Cascading bullet points means the sub-bullet woul be prefixed by parent, e.g. : `elf` -> `?dnd race elf` unless we wanna get crazy with control structures

- [ ] help -> return list of outermost heirarchy commands:

- [ ] race -> list of supported race info
 - [ ] elf ->  info about elf race
- [ ] class -> list of supported classes
  - [ ] barbarian -> info about the sorcerer class
- [ ] weapon
  - [ ] pocket-dimension-sword -> _zmp_ noise sword that can be pulled from a pocket dimension
- [ ] spell -> returns a list of the different types of spells
  - [ ] class? 
    - [ ] fireball -> info about firball cast by (class) type
- [ ] special effect (drinks/elixirs)
- [ ] dice commands
  - [x] e.g. `?dnd` xdy (x rolls of a dy) 
    - [ ] make the formatting better
- [ ] Maintain list of prefixes by server
- [ ] Maintain list of donors for... special color or quips?
- [ ] Move from local --> AWS bucket
- [ ] import -> allows the user to import homebrew material 
  - Probably done via raw JSON?  ... shouldn't accept links or files... { "race" : "new_race" [race features]
   
## Dev Guide

# Working in a branch:

Your branch is like your version of the remote (master)

create branch with `git branch name-of-your-branch`.  This will create a copy of whatever branch you're currently in (master) 

Switch out of master and into your branch with `git checkout name-of-your-branch`.  You can verify you correctly switched branches with `git branch` which will highlight the branch you're currently in

push changes from your local git repo to your remote branch with:
- `git add .` to add all the files in the current directory and (recursively) to the staging area
- `git commit -m "brief description of what you're committing"` to package up the staged changes into a hashed commit
- `git push origin name-of-your-branch` to push your changes to your branch

From here, you'll want to open a PR from your branch into the master branch and tag one of the other devs to look over your changes and merge them into master

Once a change has been pushed to master, you'll want to update your local repo & branch accordingly with `git pull origin master` 

You'll probably need to manually review any merge conflicts (VSCode makes this easy as well as the Git Desktop tool if you're more comfy with that) and just make sure you're taking in the desired changes.  

Helps to ping your teammembers once you've pushed something to your branch that you want to be pulled into master.