# OpenScope | OpenLogger Log File Exporter

The Digilent [OpenScope](https://reference.digilentinc.com/reference/instrumentation/openscope-mz/start) and [OpenLogger](https://reference.digilentinc.com/reference/instrumentation/openlogger/start) devices can log sampled data to a binary log file. This project enables exporting that data to CSV (TODO: JSON).

Digilent provide the C++ [dlog-utils](https://github.com/Digilent/dlog-utils) utility for limited processing of OpenScope log files. As of May 2019 Digilent have not added support for the OpenLogger. The current version of dlog-utils has various log file parameters hard-coded within even though these parameters are specified within the log file header.

This project uses the awesome [Kaitai Struct](https://kaitai.io) project to define the log file structure and automatically generate a Python parsing library from that. Kaitai handles all the details of the log formatting including endianness and data types, and presents the log via a very easy to use Python class.

## References

* [dlog-utils](https://github.com/Digilent/dlog-utils) for the OpenScope log struct format
* [Digilent Technical Forums](https://forum.digilentinc.com/topic/17904-read-out-log-file-from-openlogger) for OpenLogger log struct format

## Getting Started

### Prerequisites

* Python 3
* [Kaitai Struct](https://kaitai.io), v0.9 runtime for Python
* optional: the Kaitai Struct Compiler

### Installing

As at mid-2019 the Kaitai Struct stable release, available via `pip` and so on, is v0.8. However this project requires v0.9 (in order to support the conditional `channel_map` instance). The installation instructions here describe how to install 0.9 from unstable. Once 0.9 is released to stable things will be simpler.

#### Installing the Kaitai Struct Python Runtime

The Python runtime is required in order to use this project.

The runtime is available from Github and though there doesn't appear to be a branch dedicated to the 0.9 release the version as of [0e3f6e0](https://github.com/kaitai-io/kaitai_struct_python_runtime/commit/0e3f6e0ae7406af5aef2067956e13c02c31f288c) updates the package to 0.9 and works for us.

```sh
$ pip install -e 'git+https://github.com/kaitai-io/kaitai_struct_python_runtime.git@0e3f6e0#egg=kaitaistruct'
```

Once v0.9 is released to stable you should be able to just install the package via `pip`, e.g. `pip install kaitaistruct`.

#### Installing the Kaitai Struct Compiler (KSC)

Unless you're intending to work on the log file format definition you can skip this section. The source `.ksy` and KSC-compiled `.py` library are both included here so you don't need to install KSC unless you want to rebuild the `dlog.py` library.

1. Download `kaitai-struct-compiler-0.9-SNAPSHOT20190426.041158.38860dbb` from https://kaitai.io/#download
  * review the requirements (Linux/macOS/Windows and a Java runtime)
2. Unpack the archive

Once v0.9 is released to stable you should be able to just install the package from your favourite package manager, e.g. `brew install kaitai-struct-compiler`.

Invoking the compiler:
```sh
$ kaitai-struct-compiler --target python dlog.ksy
```

### Tests

TBD

Note that this code has not been tested with OpenScope logs beyond the single log file example included in the Digilent dlog-utils project.

### Usage

In its simplest form, invoking `dlogcsv.py` will read in the binary log file given as an argument, and spit out the data as CSV on stdout. A summary of the log file meta data is reported on stderr. The output CSV will include two "header" rows by default:

* the log file header fields
* the column headers

Both can be suppressed if required, see `dlogcsv.py -h` for details.

```sh
$ ./dlogcsv.py ./examples/openlogger.dlog > openlogger.csv
Header Information
log format: openlogger
stop reason: normal
number of samples: 27097
voltage units: mV
sample rate: 10E+3 Sa/s
delay: 0 s
number of channels: 3
channel map: [1, 2, 3]
```

## Attribution

This work is not affiliated with Digilent in any way.
