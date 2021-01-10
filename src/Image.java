import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Image {

    private String lien;
    private BufferedImage img;

    public Image(String lien)throws IOException
    {
        this.lien = lien;
        img = ImageIO.read(new File(this.lien));
    }

    private Image binarisation()
    {
        return null;
    }

    public Image seuillage(int seuil)
    {
        return null;
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
        return null;
    }

    public Image dilatation()
    {
        return null;
    }

    public Image ouverture()
    {
        return null;
    }

    public Image fermeture()
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
