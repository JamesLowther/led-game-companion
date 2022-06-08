import os

ASSETS_BASE = os.path.join(os.path.dirname(__file__), "assets")
COURSES_PATH = os.path.join(ASSETS_BASE, "courses")
CUPS_PATH = os.path.join(ASSETS_BASE, "cups")

CUPS = {
    "Mushroom Cup": {
        "path": os.path.join(CUPS_PATH, "mushroom.png"),
        "courses": {
            "Luigi Circuit": {
                "path": os.path.join(COURSES_PATH, "luigi-circuit.png")
            },
            "Moo Moo Meadows": {
                "path": os.path.join(COURSES_PATH, "moo-moo-meadows.png")
            },
            "Mushroom Gorge": {
                "path": os.path.join(COURSES_PATH, "mushroom-gorge.png")
            },
            "Toad's Factory": {
                "path": os.path.join(COURSES_PATH, "toads-factory.png")
            }
        }
    },
    "Flower Cup": {
        "path": os.path.join(CUPS_PATH, "flower.png"),
        "courses": {
            "Mario Circuit": {
                "path": os.path.join(COURSES_PATH, "mario-circuit.png")
            },
            "Coconut Mall": {
                "path": os.path.join(COURSES_PATH, "coconut-mall.png")
            },
            "DK Summit": {
                "path": os.path.join(COURSES_PATH, "dk-summit.png")
            },
            "Wario's Gold Mine": {
                "path": os.path.join(COURSES_PATH, "warios-gold-mine.png")
            }
        }
    },
    "Star Cup": {
        "path": os.path.join(CUPS_PATH, "star.png"),
        "courses": {
            "Daisy Circuit": {
                "path": os.path.join(COURSES_PATH, "daisy-circuit.png")
            },
            "Koopa Cape": {
                "path": os.path.join(COURSES_PATH, "koopa-cape.png")
            },
            "Maple Treeway": {
                "path": os.path.join(COURSES_PATH, "maple-treeway.png")
            },
            "Grumble Volcano": {
                "path": os.path.join(COURSES_PATH, "grumble-volcano.png")
            }
        }
    },
    "Special Cup": {
        "path": os.path.join(CUPS_PATH, "special.png"),
        "courses": {
            "Dry Dry Ruins": {
                "path": os.path.join(COURSES_PATH, "dry-dry-ruins.png")
            },
            "Moonview Highway": {
                "path": os.path.join(COURSES_PATH, "moonview-highway.png")
            },
            "Bowser's Castle": {
                "path": os.path.join(COURSES_PATH, "bowsers-castle.png")
            },
            "Rainbow Road": {
                "path": os.path.join(COURSES_PATH, "rainbow-road.png")
            }
        }
    },
    "Shell Cup": {
        "path": os.path.join(CUPS_PATH, "shell.png"),
        "courses": {
            "GCN Peach Beach": {
                "path": os.path.join(COURSES_PATH, "gcn-peach-beach.png")
            },
            "DS Yoshi Falls": {
                "path": os.path.join(COURSES_PATH, "ds-yoshi-falls.png")
            },
            "SNES Ghost Valley 2": {
                "path": os.path.join(COURSES_PATH, "snes-ghost-valley-2.png")
            },
            "N64 Mario Raceway": {
                "path": os.path.join(COURSES_PATH, "n64-mario-raceway.png")
            }
        }
    },
    "Banana Cup": {
        "path": os.path.join(CUPS_PATH, "banana.png"),
        "courses": {
            "N64 Sherbert Land": {
                "path": os.path.join(COURSES_PATH, "n64-sherbert-land.png")
            },
            "GBA Shy Guy Beach": {
                "path": os.path.join(COURSES_PATH, "gba-shy-guy-beach.png")
            },
            "DS Delphino Square": {
                "path": os.path.join(COURSES_PATH, "ds-delphino-square.png")
            },
            "GCN Waluigi Stadium": {
                "path": os.path.join(COURSES_PATH, "gcn-waluigi-stadium.png")
            }
        }
    },
    "Leaf Cup": {
        "path": os.path.join(CUPS_PATH, "leaf.png"),
        "courses": {
            "DS Desert Hills": {
                "path": os.path.join(COURSES_PATH, "ds-desert-hills.png")
            },
            "GBA Bowser Castle 3": {
                "path": os.path.join(COURSES_PATH, "gba-bowser-castle-3.png")
            },
            "N64 DK's Jungle Parkway": {
                "path": os.path.join(COURSES_PATH, "n64-dks-jungle-parkway.png")
            },
            "GCN Mario Circuit": {
                "path": os.path.join(COURSES_PATH, "gcn-mario-circuit.png")
            }
        }
    },
    "Lightning Cup": {
        "path": os.path.join(CUPS_PATH, "lightning.png"),
        "courses": {
            "SNES Mario Circuit 3": {
                "path": os.path.join(COURSES_PATH, "snes-mario-circuit-3.png")
            },
            "DS Peach Gardens": {
                "path": os.path.join(COURSES_PATH, "ds-peach-gardens.png")
            },
            "GCN DK Mountain": {
                "path": os.path.join(COURSES_PATH, "gcn-dk-mountain.png")
            },
            "N64 Bowser's Castle": {
                "path": os.path.join(COURSES_PATH, "n64-bowsers-castle.png")
            }
        }
    }
}
