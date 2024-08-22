# **⚾ PitcherPicker ⚾**

- Implementing in a script:
    Importing:
    ```sh
    from create_player_dictionary import main
    ```
    Default Usage:
    ```sh
    main()
    ```
    Specifying File Name:
    ```sh
    main("players")
    ```
    Choosing to update list of players
    ```sh
    main("players",True)
    ```
#
#

- Command line syntax:
    
    > -fn  : Defines the file name that the dictionary will be saved under
    > -names  : Specifies whether the list of desired player names should be updated
  #
    ```sh
    python3 create_player_dictionary.py -fn "{file_name}" -names {true/false}
    ```
