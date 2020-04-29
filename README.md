# 5e-DND-CATALOG
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
