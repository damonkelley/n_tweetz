# n_tweetz
Get the last n tweets of a user. (a.k.a A Docker image for demonstration purposes)

### Running

Using the default CMD
```sh
docker run --rm -e "N=10" -e "USERNAME=<username>" -e "TWITTER_SECRET" -e "TWITTER_KEY"  damonkelley/n_tweetz
```

With color output
```sh
docker run --rm -e "N=10" -e "USERNAME=<username>" -e "TWITTER_SECRET" -e "TWITTER_KEY" -t  damonkelley/n_tweetz
```

Explicitly providing the CMD (with colored output)
```sh
docker run --rm -e "TWITTER_SECRET" -e "TWITTER_KEY" -t damonkelley/n_tweetz python n_tweetz.py <args>
```
