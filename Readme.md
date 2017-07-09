Musicorum
=========

A Mac OS X app that triggers actions (only playing MP3s in the first version), when someone scans an RFID card on a plug-and-play RFID reader.

RFID Reader
-----------
[Example reader](https://www.amazon.co.uk/Neuftech-Reader-125KHZ-EM4100-Contactless/dp/B018OYOR3E/ref=sr_1_2?ie=UTF8&qid=1499622392&sr=8-2&keywords=rfid+reader+plug+and+play).

Install & Setup
---------------
1. Drag the Musicorum app into you Applications folder.
1. Create a Media folder containing MP3s you want to play. The default location is `~/Documents/MusicorumMedia`.
1. If you are using a different location edit the file `/Applications/musicorum.app/Contents/MacOS/launch.sh` and replace `~/Documents/MusicorumMedia` with the path to the folder you are using.
1. Copy all the Media files you want to able play into the Media folder (only MP3s in this version).
1. Create a file inside the Media folder called `data.tsv`.
1. This is a Tab-Separated-Value file. There is one line for every RFID card you want to use. The format for a line is `Card ID	Action	(Argument)`. Currently only two actions are supported: `play`, which takes the name of a file as an argument and `stop` which takes no arguments. A typical file would look like this:
   ```
   0012845757	play	ShakeItOff.mp3
   0006119194	stop
   ```
1. Launch Musicorum by clicking on the Icon, and you're good to go.