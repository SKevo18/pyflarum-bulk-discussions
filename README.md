# pyFlarum Bulk Discussions

A [pyFlarum](https://discuss.flarum.org/d/28221) script that allows for bulk creation of discussions from text files under `/discussions`.

## Usage

Download/clone this repository. `cd` into repository root.

Put your text files you'd wish to create as discussions in `/discussions`.
The file name (without extension) will be used as the title of the discussion. The file contents will be used as the body of the discussion. Markdown format is supported.

```bash
python -m bulk_discussions -f <your forum URL> -u <your account username> -p <account password>
```

Example:

```bash
python -m bulk_discussions -f https://flarum.example.com -u admin -p cooladmin123
```

## Disclaimer

By absolutely no means I support any malicious use of this script in order to create unwanted content/spam.
I made this script as an option to solve a problem described in [this discussion](https://discuss.flarum.org/d/30722), and I am not responsible for any damage caused by this script. You are solely responsible for your own actions.

If you feel that you are a victim of the improper use of this tool, you can block the `pyflarum` user agent at the server where your Flarum instance is hosted on, which will effectively block all traffic made by this script.

<a href="https://www.buymeacoffee.com/skevo"><img src="https://img.buymeacoffee.com/button-api/?text=Support me&emoji=🐣&slug=skevo&button_colour=ffa200&font_colour=000000&font_family=Poppins&outline_colour=000000&coffee_colour=FFDD00" /></a>
