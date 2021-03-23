[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">getIPs CLI tool</h3>

  <p align="center">
    Small python cli tool for getting all IPS from list of domains
    <br />
</p>

```bash @@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@    @@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@  @@@  @@@@@@@@  @@@@@@@   
!@@        @@!         @@!    @@!  @@!  @@@  !@@       
!@!        !@!         !@!    !@!  !@!  @!@  !@!       
!@! @!@!@  @!!!:!      @!!    !!@  @!@@!@!   !!@@!!    
!!! !!@!!  !!!!!:      !!!    !!!  !!@!!!     !!@!!!   
:!!   !!:  !!:         !!:    !!:  !!:            !:!  
:!:   !::  :!:         :!:    :!:  :!:           !:!   
 ::: ::::   :: ::::     ::     ::   ::       :::: ::   
 :: :: :   : :: ::      :     :     :        :: : :    
```      


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is very simple tool to scratch all available IP addresses from the hostname file that you will provide as a parameter. There is realy nothing special in this software, just a very simple tool that can become as a part of your recon workwflow.
Maybe some features will be added later, but you go ahead an fork and create pull request.

<!-- GETTING STARTED -->
## Installation

The tool installation is simple if you already have a `python` and `pip` installed
```bash
pip install getips
```

<!-- USAGE EXAMPLES -->
## Usage

Here is how to use this tool:

```bash
getips -h # Show help
```

```bash
getips -d path/to/domains/list # input file with domains should be a list
```

```bash
getips -d path/to/domains/list -o output_file # to save the ip's list as output file
```

```bash
getips -d domains -o ips -v # verbose output
```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

n4Zz2 - [@_n4Zz2_](https://twitter.com/_n4Zz2_) - root@n4zz2.com


[contributors-url]: https://github.com/n4Zz2/getips/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/n4Zz2/getips.svg?style=for-the-badge
[forks-url]: https://github.com/n4Zz2/getips/network/members
[stars-shield]: https://img.shields.io/github/stars/n4Zz2/getips.svg?style=for-the-badge
[stars-url]: https://github.com/n4Zz2/getips/stargazers
[issues-shield]: https://img.shields.io/github/issues/n4Zz2/getips.svg?style=for-the-badge
[issues-url]: https://github.com/n4Zz2/getips/issues
[license-shield]: https://img.shields.io/github/license/n4Zz2/getips.svg?style=for-the-badge
[license-url]: https://github.com/n4Zz2/getips/blob/master/LICENSE.txt

