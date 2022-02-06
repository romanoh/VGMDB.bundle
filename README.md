## VGMDB Plex Metadata Agent

This plugin will allow you to use VGMDB metadata for a Plex music library.

### Installation

- Download and extract the [latest release](https://github.com/matthewdias/VGMDB.bundle/releases/latest).
- Move `VGMDB.bundle` to your Plex [plugins directory](https://support.plex.tv/articles/201106098-how-do-i-find-the-plug-ins-folder/).
- Restart Plex

or

1. Clone (or unzip) this project into your Plex `Plug-ins` directory:

```
git clone https://github.com/romanoh/VGMDB.bundle.git
```

2. Restart your Plex Media Server.

For future updates, run the below commmand from within the `VGMDB.bundle` folder.

```
git pull
```

### Usage

To use the agent, create a new basic music library in Plex and select VGMDB as the metadata agent. If you want to enable track renaming, enter your Plex token in the agent settings. This will only work for single-disc albums.

### Acknowledgements

Thanks to https://github.com/hufman/vgmdb for making VGMDB data usable.
