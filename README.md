# Docker + Python (w/ pandas, numpy, etc) Example

This is a small example illustrating a Docker-based Python application
that loads/updates/persists a state file.

The example merely appends a timestamp and a random integer to a persisted pandas dataframe on every run.

## Installation

Install [Docker](https://www.docker.com/get-docker) for your system.

Clone this repository using [Git](https://git-scm.com):

``` shell
$ git clone https://github.com/bruce/docker_pydata_example.git
```

## Building it

Change into the directory:

``` shell
$ cd docker_pydata_example
```

Build the docker image with `make`:

``` shell
$ make build
```

(This may take awhile the first time, as it needs to grab the base images.)

## Running it

Run it with `make`:

``` shell
$ make run
```

You'll see something like this:

```
$ make run
mkdir -p data
docker run -v /home/bruce/code/github/bruce/docker_pydata_example/data:/app/data pydata_example
      timestamp  value
0  1.531632e+09   73.0

```

Try this several times, and you'll watch the output grow (the script adds an entry to its state on every run):

```
$ make run
mkdir -p data
docker run -v /home/bruce/code/github/bruce/docker_pydata_example/data:/app/data pydata_example
      timestamp  value
0  1.531632e+09   73.0
1  1.531632e+09   90.0
2  1.531632e+09   48.0
3  1.531632e+09   15.0
4  1.531633e+09   75.0
```

## Exploring it

See:

- The `Dockerfile`, a whopping three lines that defines the base image (`FROM`), what files to add to the image (`ADD`), and what default command to execute (`CMD`).
- The application itself, under `example/` (it's a pretty simple application, more functional then elegant or well-structured!)
- The `Makefile`, which defines how `make` builds the image and runs the container (creating and mounting a data directory, `data/`, as persistent storage across runs)
- After running it, the `data/` directory, containing `state.pkl`.

## Modifying it

Change the application (`example/`) however you'd like, then just run:

``` shell
$ make
```

This will run the default task (`all`) which does a `make build` and `make run` in quick succession.

## Resetting the data

You can clear the data with one command:

``` shell
$ make clobber
```

Then your uses of `make run` will start from a clean slate (an empty dataframe, that is).
