<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![License][license-shield]][license-url]



# Smart Trashcan



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contributors](#contributors)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Credits](#credits)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
## About The Project

Smart Trashcan is a simple program aimed at powering up your recycling using IoT and *Machine Learning*.

### Built With

* [Python](https://www.python.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [InfluxDB](https://www.influxdata.com/)


## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/carloslago">
        <img src="https://avatars2.githubusercontent.com/u/15263623?s=400&v=4" 
        width="150px;" alt="Carlos Lago"/><br/><sub><b>Carlos Lago</b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/rafaelromon">
        <img src="https://avatars0.githubusercontent.com/u/15263554?s=400&v=4" 
        width="150px;" alt="Rafael Romón"/><br /><sub><b>Rafael Romón</b></sub></a><br/></td>
  </tr>
</table>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* Python and Supporting Packages
```sh
sudo apt install python3 python3-dev
sudo apt-get install libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5 libqt4-test
```

* InfluxDB

```sh
sudo apt install influxdb
sudo apt-get install libatlas-base-dev libjasper-dev libqtgui4 python3-pyqt5 libqt4-test
```

* Tensorflow and Keras

  To install tensorflow and keras in your RPi3 you should try following a in-depth guide, as it is fairly complicated.


### Installation
 
1. Clone the repo
```sh
git clone https://github.com/rafaelromon/smart-trashcan
```
2. Install Python packages, you may need to include the --no-cache-dir flag.
```sh
sudo pip install -r requirements.txt
```

3. [Configure InfluxDB](https://docs.influxdata.com/influxdb/v1.7/introduction/getting-started/) and edit setting.py

<!-- USAGE EXAMPLES -->
## Usage

You can run this project as a normal Flask website 

```sh
python3 app.py
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CREDITS -->
## Credits

* This project started as a fork of [miguelgrinberg/flask-video-streaming](https://github.com/miguelgrinberg/flask-video-streaming)
* The bootstrap template we use for the flask site is [Gentellela by Colorlib](https://github.com/ColorlibHQ/gentelella)


<!-- CONTACT -->
## Contact

If you are not that tech savvy feel free to send us any bug reports, ask me any questions or request any features via email, just keep in mind we did this as a university project.




[license-shield]: https://img.shields.io/github/license/rafaelromon/smart-trashcan
[license-url]: https://github.com/rafaelromon/smart-trashcan/blob/master/LICENSE
