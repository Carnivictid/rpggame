from distutils.core import setup
import py2exe

setup(
console = [
{
"script": "game.py",
"icon_resources": [(1, "dndicon.ico")]
}
],
)