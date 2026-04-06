#!/usr/bin/env python3

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


def circ_imp() -> None:
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(
        f"Testing record dark spell: "
        f"{dark_spell_record('Fantasy', 'Earth, wind and fire')}"
    )
