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
* [Kaitai Struct](https://kaitai.io)

### Installing

The source `.ksy` and KSC-compiled `.py` library are both included here so you don't need to install KSC unless you want to rebuild the library.

#### macOS

```bash
% brew install kaitai-struct-compiler
% kaitai-struct-compiler --target python dlog.ksy
```

### Tests

TBD

Note that this code has not been tested with OpenScope logs beyond the single log file example included in the Digilent dlog-utils project.

### Usage

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
