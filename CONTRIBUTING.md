# Cómo colaborar en Proyecto Tifón

## Flujo de trabajo
1. Crea una rama desde `main`: `feature/<tema>-<tu-nombre>` (ej.: `feature/eda-marcos`).
2. Trabaja en Colab y guarda el notebook con **File → Save a copy in GitHub** a tu rama.
3. Si creas/edits archivos en `src/` o `tests/`, súbelos por la web de GitHub o usa git desde Colab.
4. Abre un Pull Request (PR) a `main`. Pide 1 review.
5. Merge cuando los checks estén en verde.

## Convenciones
- **Carpetas**: notebooks en `notebooks/`, código en `src/proyecto_tifon`, tests en `tests/`.
- **Nombres de notebooks**: `01_eda.ipynb`, `02_modelado.ipynb`, etc.
- **Commits**: tipo corto + descripción (ej.: `feat: EDA inicial` / `fix: normalización` / `docs:` / `refactor:`).
- **Datos**: no subir a git. Usar Drive u orígenes externos. Documentar en `data/README.md`.

## Evitar conflictos en notebooks
- Divide el trabajo por cuadernos (no editéis el mismo a la vez).
- Ideal: habilitar **Jupytext** (ver README) para tener espejo `.py` de cada `.ipynb`.

## Tests
- Ejecutar `pytest` antes del PR (en Colab: `!pytest -q`).

