# Maintainer: Edmunt Pienkowsky <roed@onet.eu>

pkgname=python-temper
pkgver=20190213
pkgrel=3
pkgdesc='Simple python library and tool for accessing TEMPer USB thermometers'
arch=('any')
url='https://github.com/urwen/temper'
license=('MIT')
depends=('python' 'python-setuptools' 'python-pyserial')
options=(!strip)
source=(
	'temper::git+https://github.com/urwen/temper.git'
	'0001-Increase-response-timeouts.patch'
	'command_line.py'
	'setup.py'
)
sha256sums=('SKIP'
            '628a06ee60b0aaae83da14e1fc01fb98041d9183a05909febc766092a57fcb6a'
            '5e043a91cb3ddc2a92c9a70877234bc7ca302c6be3163442461514fe7d0ee1e8'
            '9ae59777e23cf017324a2103047a44570208d2dfa3946495d9c463eb000da6f2')

prepare() {
	mkdir ${srcdir}/temper_py
	cd ${srcdir}/temper_py

	mkdir temper
	touch temper/__init__.py
	cp ${srcdir}/temper/temper.py temper
	cp ${srcdir}/command_line.py temper

	cd temper
	git apply ${srcdir}/0001-Increase-response-timeouts.patch
	sed -i '2d' temper.py
	chmod -x temper.py

	cd ..
	cp ${srcdir}/setup.py .
	cp ${srcdir}/temper/README.md .
}

pkgver() {
	cd ${srcdir}/temper
	git log -1 --format=%cd --date=short|tr -d -
}

build() {
	cd ${srcdir}/temper_py
	python setup.py build
}

package() {
	cd ${srcdir}/temper_py
	python setup.py install --root=${pkgdir} --optimize=2
}
