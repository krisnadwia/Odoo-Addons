{
    'name': 'Perpustakaan',
    'version': '1.0.0',
    'summary': 'Aplikasi untuk mengelola perpustakaan',
    'description': 'Mengelola data buku dan peminjam',
    'category': 'Education',
    'author': 'Ahmad Juniar',
    'website': 'stmi.ac.id',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        "view/menu.xml",
        "view/buku.xml",
        "view/pinjam.xml",
        "data/data.xml",
        "security/ir.model.access.csv",
    ],
    'installable': True,
    'application': True,
    "auto_install": False    
}