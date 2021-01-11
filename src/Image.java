import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

//http://remy-manu.no-ip.biz/Java/Tutoriels/AWT/TraitementImages.html

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

        Image imageBase = this;
        Image res = this;

        for(int i=0;i<imageBase.img.getWidth();i++)
        {
            for(int j=0;j<imageBase.img.getHeight();j++)
            {
                int color = imageBase.img.getRGB(i,j)+img.img.getRGB(i,j);

                if(color>255)
                {
                    color=255;
                }

                res.img.setRGB(i,j,color);
            }
        }
        return res;
    }

    public Image soustraction(Image img)
    {

        Image imageBase = this;
        Image res = this;

        for(int i=0;i<imageBase.img.getWidth();i++)
        {
            for(int j=0;j<imageBase.img.getHeight();j++)
            {
                int color = imageBase.img.getRGB(i,j)-img.img.getRGB(i,j);

                if(color<0)
                {
                    color=0;
                }

                res.img.setRGB(i,j,color);
            }
        }
        return res;
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

    //ajouter un paramètre L
    public Image transformationDeVoisinage()
    {
        return null;
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
