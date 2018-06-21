# TELECIRCUIT
is a website which provide opportunity to buy circuits and components for tvs. Telecircuit contains much brands such as Samsung, DELL, LG and etc. You can search an electronic catalog by keywords. Find what you need and after make an order. 
## Technology Stack
<p align="center"> 
  <img src="https://preview.ibb.co/nQ08C8/dockerdjango_big.png">
</p>

* Docker v17.04
* Docker-compose v1.21
* Django v2.0
* Webpack v4.12


### Installing
1. Install docker and docker-compose via executing build.sh script
```bash
bash build.sh
```
2. Add user to docker group to run commands without sudo
```
sudo usermod -aG docker $USER
```
3. Go to ```/telecircuit-manager``` install dependencies for frontend and run webpack

```
npm install; npm run dev
```
4. Run docker-compose to build and run containers for the application
```
docker-compose up --build
```
That's all. Now you are ready for developing. 

## Authors

* **FUNNYDMAN** - *Initial work* 

See also the list of [contributors]() who participated in this project.

Happy coding :sunglasses:
