# QR-Reader Service

This service takes bytes which represents a PNG, with a QR code in it.  It returns the decoded string from the QR code.

The reason it exists, is because parsing QR-codes requires data-science libraries that are time-consuming to build and painful to setup locally.

It's deployed to GCP, but you can run it locally too by just building the Docker image.

```
docker build . -t qrreader
docker run qrreader
```
