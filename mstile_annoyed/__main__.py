import click
from pathlib import Path
from .core import generate_mstile_icons

@click.group()
def cli():
    """Microsoft Tile icon generator for NextJS applications."""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output-dir', '-o', default='public/icons',
              help='Directory to save the generated icons (default: public/icons)')
def generate(input_file, output_dir):
    """Generate mstile icons from an input image."""
    try:
        generated_files = generate_mstile_icons(input_file, output_dir)
        click.echo(f"Successfully generated {len(generated_files)} icons:")
        for file in generated_files:
            click.echo(f"  - {file}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    cli() 