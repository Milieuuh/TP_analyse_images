import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Image {

    private String lien;
    private BufferedImage img;

    public Image(String lien) throws IOException
    {
        this.lien = lien;
        img = ImageIO.read(new File(this.lien));
    }


    public Image seuillage(int seuil)
    {
        Image imageSeuil = this;

        for (int i=0; i<this.img.getWidth(); i++)
        {
            for (int j=0; j<this.img.getHeight(); j++)
            {
                    if(this.img.getRGB(i,j)<seuil)
                    {
                        imageSeuil.img.setRGB(i, j, 0);
                    }
                    else
                    {
                        imageSeuil.img.setRGB(i, j, 255);
                    }
            }
        }

        return imageSeuil;
    }

    public Image addition(Image img)
    {
        return null;
    }

    public Image soustraction(Image img)
    {
        return null;
    }

    public Image erosion()
    {
        Image erodee = this;
        Image binaire = this.seuillage(120);
        for (int i=1; i<=binaire.img.getWidth()-2; i++)
        {
            for (int j=1; j<=binaire.img.getHeight()-2; j++)
            {
                int somme = 0;
                for(int k=-1; k<=1; k++)
                {
                    for(int l=-1; l<=1; l++)
                    {
                        somme += binaire.img.getRGB(i+k, j-l);
                    }
                }

                if(somme == 2295)
                {
                    erodee.img.setRGB(i, j, 255);
                }
                else
                {
                    erodee.img.setRGB(i, j, 0);
                }
            }
        }

        return erodee;
    }

    public Image dilatation()
    {
        Image dilatee = this;
        Image binaire = this.seuillage(120);
        for (int i=1; i<=binaire.img.getWidth()-2; i++)
        {
            for (int j=1; j<=binaire.img.getHeight()-2; j++)
            {
                int somme = 0;
                for(int k=-1; k<=1; k++)
                {
                    for(int l=-1; l<=1; l++)
                    {
                        somme += binaire.img.getRGB(i+k, j-l);
                    }
                }

                if(somme == 0)
                {
                    dilatee.img.setRGB(i, j, 0);
                }
                else
                {
                    dilatee.img.setRGB(i, j, 255);
                }
            }
        }

        return dilatee;
    }

    public Image ouverture()
    {
        Image erodee = this.erosion();
        Image result = erodee.dilatation();
        return result;
    }

    public Image fermeture()
    {
        Image dilatee = this.dilatation();
        Image result = dilatee.erosion();
        return result;
    }

    public Image amincissement()
    {
        return null;
    }

    public Image epaississement()
    {
        return null;
    }



}
