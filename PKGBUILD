# Maintainer: Edmunt Pienkowsky <roed@onet.eu>

pkgname=python-temper
pkgver=20190213
pkgrel=1
pkgdesc='Simple python library and tool for accessing TEMPer USB thermometers'
arch=('any')
url='https://github.com/urwen/temper'
license=('MIT')
depends=('python' 'python-setuptools')
optdepends=()
options=(!strip)
source=(
	'temper::git+https://github.com/urwen/temper.git'
	'command_line.py'
	'setup.py'
)
sha256sums=('SKIP'
            '5e043a91cb3ddc2a92c9a70877234bc7ca302c6be3163442461514fe7d0ee1e8'
            '9293721ab33736b3dbca6b49a3ab02b29fc4d615beda8ff473ad8c9e78a4f90c')

prepare() {
	mkdir ${srcdir}/temper_py
	cd ${srcdir}/temper_py
	mkdir temper
	touch temper/__init__.py
	cp ${srcdir}/temper/temper.py temper
	cp ${srcdir}/command_line.py temper
	sed -i '2d' temper/temper.py
	chmod -x temper/temper.py
	cp ${srcdir}/setup.py .
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
