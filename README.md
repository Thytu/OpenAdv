<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
  <a href="https://github.com/Thytu/Adversarial-attacks">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Adversarial-attacks</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/Thytu/Adversarial-attacks"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Thytu/Adversarial-attacks">View Demo</a>
    ·
    <a href="https://github.com/Thytu/Adversarial-attacks/issues">Report Bug</a>
    ·
    <a href="https://github.com/Thytu/Adversarial-attacks/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)



There are many great web interface to try adversarial attacks available on GitHub; however, I didn't find one that really suited my needs so I created this one.

Here's why:
* Simple examples to get started
* Multiple type of Adv Attacks available
* Usage of custom model (vision only) (in progress)

If you miss any type of Adv Attack please consider to fork this repo and to create a pull request or to open an issue.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [PyTorch](https://pytorch.org)
* [Gradio](https://pytorch.org)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure to use python3.9.X, torch is currently not supported for python 3.10 and native tuple type hinting has been introduced in python3.9.

Then you only need to install the python dependencies : `python3 -m pip install requirements.txt`

### Installation

1. Start the server
   ```sh
   python src/main
   ```
2. Enjoy

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To start you simply have to select the attack you want to proced among : IMask, TIMask, FGSM, TFGSM, BIM and TBIM

Then select or drag & drop the image on which you want to apply the attack and select the parameters for the attack.

TODO: describe every param
`epsilon` :  todo
`alpha` :  todo
`iterations` :  todo

### IMask
TODO: Description of the attack
Do not use `alpha` and `target`.

### TIMask
TODO: Description of the attack
Do not use `alpha`.


### FGSM
TODO: Description of the attack
Do not use `alpha`, `target` and `iterations`.

### TFGSM
TODO: Description of the attack
Do not use `alpha` and `iterations`.

### BIM
TODO: Description of the attack
Do not use `target`.

### TBIM
TODO: Description of the attack


TODO: add a conf threshold to param


<p align="right">(<a href="#top">back to top</a>)</p>


## Roadmap

- [ ] Support more attacks
    - [ ] Carlini & Wagner
    - [ ] Deepfool
- [ ] Add Changelog
- [ ] Custom Model Support

See the [open issues](https://github.com/Thytu/Adversarial-attacks/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#top">back to top</a>)</p>



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/my-feature`)
3. Commit your Changes (`git commit -m 'feat: my new feature`)
4. Push to the Branch (`git push origin feature/my-feature`)
5. Open a Pull Request

Please try to follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

<p align="right">(<a href="#top">back to top</a>)</p>



## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



## Contact

Valentin De Matos - [@ValentinDeMato1](https://twitter.com/ValentinDeMato1) - valentin.de-matos@epitech.eu

Project Link: [https://github.com/Thytu/Adversarial-attacks](https://github.com/Thytu/Adversarial-attacks)

<p align="right">(<a href="#top">back to top</a>)</p>



## Acknowledgments

* [Adversarial Attacks in Machine Learning and How to Defend Against Them](https://towardsdatascience.com/adversarial-attacks-in-machine-learning-and-how-to-defend-against-them-a2beed95f49c)
* [Pytorch - ADVERSARIAL EXAMPLE GENERATION](https://pytorch.org/tutorials/beginner/fgsm_tutorial.html)
* [README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Thytu/Adversarial-attacks.svg?style=for-the-badge
[contributors-url]: https://github.com/Thytu/Adversarial-attacks/graphs/contributors
[issues]: https://img.shields.io/github/issues/Thytu/Adversarial-attacks
[forks-shield]: https://img.shields.io/github/forks/Thytu/Adversarial-attacks.svg?style=for-the-badge
[forks-url]: https://github.com/Thytu/Adversarial-attacks/network/members
[stars-shield]: https://img.shields.io/github/stars/Thytu/Adversarial-attacks.svg?style=for-the-badge
[stars-url]: https://github.com/Thytu/Adversarial-attacks/stargazers
[issues-shield]: https://img.shields.io/github/issues/Thytu/Adversarial-attacks.svg?style=for-the-badge
[issues-url]: https://github.com/Thytu/Adversarial-attacks/issues
[license-shield]: https://img.shields.io/github/license/Thytu/Adversarial-attacks.svg?style=for-the-badge
[license-url]: https://github.com/Thytu/Adversarial-attacks/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/valentin-de-matos
[product-screenshot]: images/screenshot.png
